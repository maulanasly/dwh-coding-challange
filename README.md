### Task
1. Visualize the complete historical table view of each tables in tabular format in stdout (hint: print your table)
2. Visualize the complete historical table view of the denormalized joined table in stdout by joining these three tables (hint: the join key lies in the `resources` section, please read carefully)
3. From result from point no 2, discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction?  
   Transaction is defined as activity which change the balance of the savings account or credit used of the card

## Solution
I'm using Python, Pandas, and Petl to solve this problem because a combination of those three make implementation faster. Before starting implementation, I take a few records from each collection and play with them in a google spreadsheet to get an insight into the overall data structure. Then, after all, clear and the logic is decided, then implementation can start.

### How to run
As the solution is wrapping using docker and simplified on bash script the step to run the process, you can follow these steps:
- Simpy run `./build.sh`
- Exectute `./run.sh`
### Task 1
Solution of solving task number 1 can be find under ` === Task 1 ===` when the docker executed.
### Task 2
Solution of solving task number 2 can be find under `=== Task 2 ===` when the docker executed.
### Task 3
Solution of solving task number 3 can be found under `=== Task 3 ===` when the docker executed.
From the summary, we can see total transaction being made is 10, which contains includes
- An initial deposit of 15000 at 2020-01-02T09:00:00
- An interest rate of 1.5% because this number will affect the balance at 2020-01-04T17:31
- A credit usage 12000 from credits at 2020-01-06T12:30:00
- A credit usage 19000 from credits at 2020-01-07T18:00:00
- A deposit to saving account 40000 at 2020-01-10T09:30
- A deposit to saving account 21000 at 2020-01-10T11:00
- An interest rate of 1.5% because this number will affect the balance at 2020-01-15T09:01:00
- An interest rate of 4% because this number will affect the balance at 2020-01-17T22:01:00
- Final balance 33000 at 2020-01-20T07:30:00