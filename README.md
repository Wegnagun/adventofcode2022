# adventofcode2022

## Тут в файлы буду выкладывать мои решения задачек с мероприятия   
```
--- Day 1: Calorie Counting --- 
Santa's reindeer typically eat regular reindeer food, but they need a lot  
of magical energy to deliver presents on Christmas. For that, their favorite 
snack is a special type of star fruit that only grows deep in the jungle.  
The Elves have brought you on their annual expedition to the grove where  
the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum  
of fifty stars by December 25th. Although the Elves assure you that the grove  
has plenty of fruit, you decide to grab any fruit you see along the way,  
just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each  
day in the Advent calendar; the second puzzle is unlocked when you complete  
the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or  
access from the air; the Elves' expedition traditionally goes on foot. As  
your boats approach land, the Elves begin taking inventory of their supplies.  
One important consideration is food - in particular, the number of Calories  
each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the  
various meals, snacks, rations, etc. that they've brought with them, one item  
per line. Each Elf separates their own inventory from the previous Elf's  
inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end  
up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of  
6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000  
Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total  
of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which  
Elf to ask: they'd like to know how many Calories are being carried by the  
Elf carrying the most Calories. In the example above, this is 24000 (carried  
by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that  
Elf carrying?

--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already 
realized that the Elf carrying the most Calories of food might eventually run 
out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the 
total Calories carried by the top three Elves carrying the most Calories. That 
way, even if one of those Elves runs out of snacks, they still have two 
backups.

In the example above, the top three Elves are the fourth Elf (with 24000 
Calories), then the third Elf (with 11000 Calories), then the fifth Elf 
(with 10000 Calories). The sum of the Calories carried by these three elves 
is 45000.

Find the top three Elves carrying the most Calories. How many Calories are 
those Elves carrying in total?

--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be 
closest to the snack storage, a giant Rock Paper Scissors tournament is already 
in progress.

Rock Paper Scissors is a game between two players. Each game contains many 
rounds; in each round, the players each simultaneously choose one of Rock, 
Paper, or Scissors using a hand shape. Then, a winner for that round is 
selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats 
Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy 
guide (your puzzle input) that they say will be sure to help you win. "The 
first column is what your opponent is going to play: A for Rock, B for Paper, 
and C for Scissors. The second column--" Suddenly, the Elf is called away to 
help with someone's tent.

The second column, you reason, must be what you should play in response: X 
for Rock, Y for Paper, and Z for Scissors. Winning every time would be 
suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your 
total score is the sum of your scores for each round. The score for a single 
round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 
for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if 
the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you 
should calculate the score you would get if you were to follow the strategy 
guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose 
Paper (Y). This ends in a win for you with a score of 8 (2 because you chose 
Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose 
Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a 
score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a 
total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your 
strategy guide?

--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies 
for the jungle journey. Unfortunately, that Elf didn't quite follow the packing 
instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant 
to go into exactly one of the two compartments. The Elf that did the packing 
failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack 
(your puzzle input), but they need your help finding the errors. Every item 
type is identified by a single lowercase or uppercase letter (that is, a and 
A refer to different types of items).

The list of items for each rucksack is given as characters all on a single 
line. A given rucksack always has the same number of items in each of its two 
compartments, so the first half of the characters represent items in the first 
compartment, while the second half of the characters represent items in the 
second compartment.

For example, suppose you have the following list of contents from six 
rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means 
its first compartment contains the items vJrwpWtwJgWr, while the second 
compartment contains the items hcsFMMfFFhFp. The only item type that appears 
in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and 
rsFMfFZSrLrFZsSL. The only item type that appears in both compartments 
is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; 
the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted 
to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both 
compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), 
and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. 
What is the sum of the priorities of those item types?