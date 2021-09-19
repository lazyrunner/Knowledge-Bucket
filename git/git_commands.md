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
This stashes the current state of the branch with an index. The index can be seen by :
  
```
git stash list
  
Response:
  
stash@{0}: WIP on consistency_test: c88f335 randomization check for few algorithms
```
In case we want to <b>name our stash</b> , we use the command : 
  
```
git stash push -m "<stash_name>"
```
Doing ```git stash list``` post that will give us a similar list as above but our message 
  

  
  
  
  
  
  
 
