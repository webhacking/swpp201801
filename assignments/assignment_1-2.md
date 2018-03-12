# Assignment 1-2. Simple Calculator Continued

#### Due: 2018.03.14. 11:59PM
**Before you go through this assignment, the `add_sub` pull request should be merged.
TA will merge the pull request after you push the requested changes.**

In assignment 1-2, you will learn how to "squash" existing commits, and will resolve a conflict on the `add_mul` pull request.
Since you implemented add function in both pull requests, a conflict will outbreak once the `add_sub` pull request is merged.
To merge the `add_mul` pull request, you must resolve the conflict.

***

### STEP 1. Squashing Existing Commits
Owing to difficulty in implementing mul function, your commit log became messy.
Hence, you are going to clean up the commit log by squashing the commits before you resolve the conflict.

1. Squash the three commits, which are implementation of add function and mul function, and merge of mul_trial.
In this case, you can squash the commits in two ways, which are using `git reset` command or using `git rebase` command.
2. Push the squashed commit into the `add_mul` branch.
Since conflicting commits are already pushed into the branch, you should use forced push.
You can search for "f" option of `git push` command.

### STEP 2. Resolving the Conflict
After you squash the commits, you will resolve the conflict.

3. Pull your branch of upstream repository into your local `add_mul` branch.
This will cause a conflict on add function between your upstream branch and the `add_mul` branch.
4. Resolve the conflict by editing add function.
5. Complete the merge by commiting the conflicted file.
You don't have to change the commit message since git will leave a proper message for you.

***
