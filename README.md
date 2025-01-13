# Long-CoT-data-for-LLM-to-solve-24-puzzle
It is a sft dataset for  training LLM to solve 24(puzzle)
The code is modified from https://github.com/StephenA0/Challenge-24
# CoT dataset
run `24puzzle_cot.py` to get the CoT dataset.
example:
```
Given the numbers 3, 7, 4, 5, I should calculate step by step to get 24.\nStep 1: The most reseaonable operation is (3 - 7),  which leave 4, 5 as the remaining numbers.\nStep 2: The most reseaonable operation is ((3 - 7) * 5),  which leave 4 as the remaining numbers.\nStep 3: The last operation should be (4 - ((3 - 7) * 5)).
```

# Long CoT dataset （CoT with reflection)
run `24puzzle_longcot.py` to get the Long CoT dataset.
example:
```
Given the numbers 3, 7, 4, 5, I should calculate step by step to get 24.\nStep 1: The most reseaonable operation is (3 - 7),  which leave 4, 5 as the remaining numbers.\nStep 2: The most reseaonable operation is ((3 - 7) + 5),  which leave 4 as the remaining numbers.\nFianl Step: The last operation should be (((3 - 7) + 5) + 4).\nIt is wrong, let get back to the previous step2 and try another operation.\nNew Step 2: The most reseaonable operation is ((3 - 7) * 5),  which leave 4 as the remaining numbers.\nNew Final Step: The last operation should be (4 - ((3 - 7) * 5)).
```

# Use it to train a LLM
I use [LLaMa-factory](https://github.com/hiyouga/LLaMA-Factory) to train Qwen-2.5-0.5b-instruct to demonstrate it.
I use gpt-4o to to determine if it is correct. The test dataset is 50.
Model	| Method	| Acc (best step)
---|---|---
Qwen2.5-0.5	| w/o finetune	| 0% (-)
Qwen2.5-0.5	| SFT with CoT	| 54% (2500)
Qwen2.5-0.5	| SFT with Long CoT	| 78% (2000)

### the accuracy on test dataset
![metrics](compare.png) 

