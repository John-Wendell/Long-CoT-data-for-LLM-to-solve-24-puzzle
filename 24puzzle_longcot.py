import copy
import json
def find_all_sols(f, n, operands, op_strings,training_set=[]):

    initial_op_strings = copy.copy(op_strings)
    total = find_all_sols_recur(f, initial_op_strings, n, operands, op_strings, 0, training_set)
    
    if total == 0:
        print("No solutions.")
    else:
        print("Number of solutions: " + str(total))

#equals curr_total + number of new solutions
def find_all_sols_recur(f, initial_op_strings, n, operands, op_strings, curr_total,training_set, history_item=[], history_left=[]):

    # print('history_item',history_item)
    #n: Goal value
    #operands: List of integer operands
        #Math performed on this list
    #op_strings: String form of operands
        #Tracks performed operations
        #Ex. operands = [6, 7] may mean op_strings = ["(3 * 2)", "(2 + 5)"]
    #curr_total: running total of successes
    
    # if len(operands) == 1 and n == operands[0]:
    if len(operands) == 1:
        # print('operands',operands)
        # print(op_strings[0])
        # print('history_item',history_item)
        # print('history_left',history_left)
        curr_total = curr_total + 1
        # history_set.append(history_item)
        # write to json

        prompt = 'Given the numbers ' + ', '.join(initial_op_strings) + ', I should calculate step by step to get ' + str(n) + '.\n'
        for i in range(len(history_item)-1):
            prompt += 'Step ' + str(i+1) + ': ' 
            prompt += 'The most reseaonable operation is ' + history_item[i] + ', '
            # print('history_left',history_left[i])
            prompt += ' which leave ' + ', '.join(map(str,history_left[i])) + ' as the remaining numbers.\n'
        prompt += 'Fianl Step: '
        prompt += 'The last operation should be ' + history_item[-1] + '.'
        # print(prompt)
        sample = {'output': prompt}
        sample['input'] = ''
        instruction = 'Given the numbers ' + ', '.join(initial_op_strings) + '. ' +'Use numbers and basic arithmetic operations (+ - * /) to obtain ' + str(n) + '.\n'
        sample['instruction'] = instruction
        if n == operands[0]:
            sample['label'] = 1
        else:
            sample['label'] = 0
        sample['history_item'] = history_item
        sample['history_left'] = history_left 
        sample['initial_op_strings'] = ', '.join(initial_op_strings)
        training_set.append(sample)

        
    else:
        if len(operands) == 4:
            history_item = []
            history_left = []
            # initial_op_strings = copy.copy(op_strings)
        for j in range(len(operands)):

            for i in range(j):
                
                # if j < len(operands) - 1:
                # print('i',i)
                # print('j',j)
                #     print('len(operands)',len(operands))
                #     print('operands_beofre',operands)
                #     print('op_strings_before',op_strings)
                tempi = operands[i]
                tempj = operands[j]
                # if j < len(operands) - 1:
                #     print('tempi',tempi)
                #     print('tempj',tempj)
                strtempi = op_strings[i]
                strtempj = op_strings[j]
                # if j < len(operands) - 1:
                #     print('strtempi',strtempi)
                #     print('strtempj',strtempj)
                operands[j] = operands[len(operands) - 1] #need only consider operands[:-1], tempj
                op_strings[j] = op_strings[len(op_strings) - 1] #need only consider op_strings[:-1], strtempj
                # if j < len(operands) - 1:
                #     print('operands',operands)
                #     print('op_strings',op_strings)

                operands[i] = tempi + tempj
                op_strings[i] = "(" + strtempi + " + " + strtempj + ")"
                # print('operands',op_strings[i])
                # print('history_item',history_item)
                history_item_1 = copy.copy(history_item)
                history_left_1 = copy.copy(history_left)
                # print('history_item_1',history_item_1)
                history_item_1.append(op_strings[i])

                
                history_left_item_1 = copy.copy(operands)
                # print('history_left_1',history_left_1)
                history_left_item_1.remove(operands[i])
                history_left_item_1.remove(operands[j])
                # print('history_left_1',history_left_1)
                # print('history_item_1',history_item_1)
                history_left_1 = copy.copy(history_left)
                history_left_1.append(history_left_item_1)
                curr_total = find_all_sols_recur(f, initial_op_strings, n, operands[:-1], op_strings[:-1], curr_total,training_set, history_item_1, history_left_1)
                
                operands[i] = tempi - tempj
                op_strings[i] = "(" + strtempi + " - " + strtempj + ")"
                history_item_1 = copy.copy(history_item)
                history_item_1.append(op_strings[i])
                history_left_item_1 = copy.copy(operands)
                # print('history_left_1',history_left_1)
                history_left_item_1.remove(operands[i])
                history_left_item_1.remove(operands[j])
                history_left_1 = copy.copy(history_left)
                history_left_1.append(history_left_item_1)
                curr_total = find_all_sols_recur(f, initial_op_strings, n, operands[:-1], op_strings[:-1], curr_total,training_set, history_item_1, history_left_1)

                operands[i] = tempj - tempi
                op_strings[i] = "(" + strtempj + " - " + strtempi + ")"
                history_item_1 = copy.copy(history_item)
                history_item_1.append(op_strings[i])
                history_left_item_1 = copy.copy(operands)
                # print('history_left_1',history_left_1)
                history_left_item_1.remove(operands[i])
                history_left_item_1.remove(operands[j])
                history_left_1 = copy.copy(history_left)
                history_left_1.append(history_left_item_1)
                curr_total = find_all_sols_recur(f, initial_op_strings, n, operands[:-1], op_strings[:-1], curr_total,training_set, history_item_1, history_left_1)

                operands[i] = tempi * tempj
                op_strings[i] = "(" + strtempi + " * " + strtempj + ")"
                history_item_1 = copy.copy(history_item)
                history_item_1.append(op_strings[i])
                history_left_item_1 = copy.copy(operands)
                # print('history_left_1',history_left_1)
                history_left_item_1.remove(operands[i])
                history_left_item_1.remove(operands[j])
                history_left_1 = copy.copy(history_left)
                history_left_1.append(history_left_item_1)
                curr_total = find_all_sols_recur(f, initial_op_strings, n, operands[:-1], op_strings[:-1], curr_total,training_set, history_item_1, history_left_1)

                if tempj != 0: #prevents division by zero
                    operands[i] = tempi / tempj
                    op_strings[i] = "(" + strtempi + " / " + strtempj + ")"
                    history_item_1 = copy.copy(history_item)
                    history_item_1.append(op_strings[i])
                    history_left_item_1 = copy.copy(operands)
                    # print('history_left_1',history_left_1)
                    history_left_item_1.remove(operands[i])
                    history_left_item_1.remove(operands[j])
                    history_left_1 = copy.copy(history_left)
                    history_left_1.append(history_left_item_1)
                    curr_total = find_all_sols_recur(f, initial_op_strings, n, operands[:-1], op_strings[:-1], curr_total,training_set,history_item_1, history_left_1)

                if tempi != 0: #prevents division by zero
                    operands[i] = tempj / tempi
                    op_strings[i] = "(" + strtempj + " / " + strtempi + ")"
                    history_item_1 = copy.copy(history_item)
                    history_item_1.append(op_strings[i])
                    history_left_item_1 = copy.copy(operands)
                    # print('history_left_1',history_left_1)
                    history_left_item_1.remove(operands[i])
                    history_left_item_1.remove(operands[j])
                    history_left_1 = copy.copy(history_left)
                    history_left_1.append(history_left_item_1)
                    curr_total = find_all_sols_recur(f, initial_op_strings, n, operands[:-1], op_strings[:-1], curr_total,training_set,history_item_1, history_left_1)

                #Method terminated: reset variables
                operands[i] = tempi 
                operands[j] = tempj
                op_strings[i] = strtempi
                op_strings[j] = strtempj
        
    return curr_total


# N = input("N?   ")
N = 24
try:
    N = int(N)
except:
    print("Please input an integer.")

# vals = input("Values? (separate each by a space)     ").split(" ")
# random choose 4 numbers from 1 to 13
import random
# set random seed
random.seed(44)
with open('24puzzle_train_l.json', 'w') as f:
    training_set_new = []
    for i in range(50):
        training_set = []
        vals = random.sample(range(1, 14), 4)
        vals = list(map(str, vals))
        find_all_sols(f, N, list(map(int, vals)), vals,training_set) 
        
    
        for i in range(len(training_set)):
            if training_set[i]['label'] == 0:
                for j in range(len(training_set)):
                    if training_set[j]['label'] == 1 and training_set[i]['initial_op_strings'] == training_set[j]['initial_op_strings']:
                        flage = 0
                        for k in range(len(training_set[i]['history_item'])-1):
                            k_r = len(training_set[i]['history_item']) - k - 1
                            if training_set[i]['history_item'][:k_r] == training_set[j]['history_item'][:k_r]:
                                new_item = copy.deepcopy(training_set[i])
                                new_item['output'] += '\n' + 'It is wrong, let get back to the previous step' + str(k_r+1) + ' and try another operation.\n'
                                for l in range(len(training_set[i]['history_item']) - k_r - 1):
                                    new_item['output'] += 'New Step ' + str(l+1+k_r) + ': ' 
                                    new_item['output'] += 'The most reseaonable operation is ' + training_set[j]['history_item'][l+k_r] + ', '
                                    new_item['output'] += ' which leave ' + ', '.join(map(str,training_set[j]['history_left'][l+k_r])) + ' as the remaining numbers.\n'
                                new_item['output'] += 'New Final Step: ' + 'The last operation should be ' + training_set[j]['history_item'][-1] + '.'
                                new_item['label'] = 1
                                flage = 1
                                break
                        if flage == 1:
                            training_set_new.append(new_item)
                            break
            elif training_set[i]['label'] == 1:
                training_set_new.append(training_set[i])

                
        
    
    
    print('training_set length',len(training_set_new))
    json.dump(training_set_new, f, indent=2)
# vals = ['1', '2', '3', '4']
# print(vals)
# print(list(map(int, vals)))
# break
# find_all_sols(N, list(map(int, vals)), vals) 
# try:
#     find_all_sols(N, list(map(int, vals)), vals) 
#     break
# except: 
#     print("Please input integer values separated by spaces.")
