# Assignment 1-1. Simple Calculator

#### Due: 2018.03.09. 11:59PM
You will implement a simple calculator to practice Git and GitHub.
The calculator supports addition, subtraction, and multiplication.
Your task is to implement three functions, `add(int a, int b)`, `sub(int a, int b)`, and `mul(int a, int b)`.
Every student should send 2 pull requests to their own branch, named as student ID's last 5 digits, of [upstream repository](https://github.com/snu-sf-class/SWPP2018_Git_Assignment).
Please follow the following instructions.

***

### STEP 1
1. Fork the [upstream repository](https://github.com/snu-sf-class/SWPP2018_Git_Assignment).
You will work on your repository (your fork).
2. Clone your fork and checkout to your own branch.
Your branch is containing skeleton code of the calculator.
3. Create two branches named `add_sub` and `add_mul`, on which you will work.

### STEP 2
4. Switch to the `add_sub` branch and implement two functions `add(int a, int b)` and `sub(int a, int b)` on it.
While you are working, first, implement `add(int a, int b)` and commit, and then, implement `sub(int a, int b)` and commit again,
i.e., the number of commits should be 2.
5. Push the `add_sub` branch to your repository.
6. Make a pull request to your branch of [upstream repository](https://github.com/snu-sf-class/SWPP2018_Git_Assignment) from your `add_sub` branch.

### STEP 3
7. Switch to the `add_mul` branch.
You will Implement two functions `add(int a, int b)` and `mul(int a, int b)` on this branch.
8. Implement `add(int a, int b)` function in a different way (e.g., make it recursively) from step 4, and commit.
9. Since multiplication is a difficult task, you wish to make 2 trials on implementing it.
Create two branches named `mul_trial_1` and `mul_trial_2`.
10. Implement `mul(int a, int b)` on each branch and commit on both branches.
After the commit, push the branches to your repository.
11. You realized that your first trial, which implemented on `mul_trial_1`, is wrong.
Thus, you should merge `mul_trial_2` branch into `add_mul` branch.
To do this, you should first checkout to the `add_mul` branch and merge the `mul_trial_2` branch into it.
When you merge two branches, please **DO NOT USE** 'fast-forward' merge.
You can search what 'fast-forward' is and how to avoid it.
12. Push the `add_mul` branch to your repository.
13. Make another pull request to your branch of
[upstream repository](https://github.com/snu-sf-class/SWPP2018_Git_Assignment) from your `add_mul` branch.

### Note
- Please leave some descriptions on pull requests, which explain what you have done on each pull request.

***

After the due date, TA will review the pull requests and request some modification.
If you receieve comments, please read it, modify as requested, and comment back to TAs.
Next assignment will be announced on Monday(03.12.)
