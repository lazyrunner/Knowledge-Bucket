# Git Commands

Git commands for daily functioning. 

## Author Sudeshna Bora

---

### Command 1 : Fetch remote branch to work on it 

#### Step 1 : 

```
git branch -r
```
This gives all the remote branch for this repository.

#### Step 2: 

```
git fetch
```
This fetches all information (commits, files, refs) from remote to local.

#### Step 3:

```
git checkout -b <name of branch> <remote>/<name of branch>

Ex:
git checkout -b test origin/test
```
This checkouts out the remote branch <remote>/<name of branch> to the local branch named <name of branch>
  
Post this, if we do ```git branch``` , we should get the newly checkout branch in the local list. 
  
---
### Command 2 : Stashing progress
  
When we are working on a branch and we need to ```checkout``` into another branch or update our branch, it is imperative for us to shelf our current
changes so that it is not lost with the updation. ```git stash``` is used for shelfing our changes.
  
#### Command to stash : 
  
```
git stash
```
This stashes the current state of the branch with an index. 
In case we want to name our comment our stash, we can use:
  
```
git stash push -m "<stash_name>"
```
  
The list of stashes can be seen by :
  
```
git stash list
  
Response:
  
stash@{0}: WIP on consistency_test: c88f335 randomization check for few algorithms
```

There are two ways to apply the git stash into the current directory. 
  
```
git stash apply
```
  
```
git stash pop
```
The difference between the first and the second command is that with ```apply```, the entry into the stash is not deleted whereas for ```pop``` 
we delete the entry from the stash. 
  
We also know , the stash entries are indexed and we can also give our custom identifier. 
So, we can use these indices or custom identifiers to get a particular stash.
  
```
git stash pop stash@{n}

git stash apply stash@{n}
  
Here, n is the index number

git stash apply stash^{/message}
```
  
---

  

  
  
  
  
  
  
 
