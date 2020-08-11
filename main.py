## Importing Libraries
from gpt import GPT
from gpt import Example
from gpt import set_openai_key

## Creating GPT-3 Object with some custom parameters
gpt = GPT(
    engine="davinci",
    temperature=0.5,
    max_tokens=100
)


## Setting OpenAI api key 
set_openai_key("YOUR_OPENAI_KEY")

file = open('data.txt', 'r')
content = file.read()

## Adding Examples to the GPT-e from data.txt file
for line in content.split('\n'):
    
    if line.startswith('- '):
        inp = line[2:]
    else:
        out = line[2:]
        ex = Example(input= inp, output=out)
        gpt.add_example(ex)
        
        
if __name__ == "__main__":
    query = input("Enter a query to convert ==> ")
    while query:
        output = gpt.submit_request(query)
        print(output.choices[0].text)
        sentence = input("Enter another query to convert ==> ")
        
        