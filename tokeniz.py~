from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

tokenizer = Tokenizer(BPE())
trainer = BpeTrainer(vocab_size=6000 , min_frequency=2)



test_data = ["my name is what", "my name is wha", "chika chika slim slady "]
tokenizer.train_from_iterator(test_data, trainer)

output = tokenizer.encode("my name is what slim chika")

print(output.tokens)
