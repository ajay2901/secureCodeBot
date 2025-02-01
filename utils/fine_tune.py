# utils/fine_tune.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

def fine_tune_model(dataset, model_name, output_dir="./fine_tuned_model"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=1)
    
    # Preprocess dataset
    def preprocess_data(examples):
        return tokenizer(examples['Question'], truncation=True, padding="max_length", max_length=128)
    
    tokenized_dataset = dataset.map(preprocess_data, batched=True)
    tokenized_dataset = tokenized_dataset.remove_columns(['Question', 'Answer'])
    tokenized_dataset.set_format("torch")
    
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=1,
        logging_dir="./logs",
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset,
    )
    
    trainer.train()
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

    print(f"Model fine-tuned and saved to {output_dir}")
    return model, tokenizer
