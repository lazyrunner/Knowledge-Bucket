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
 
### Stashing progress
  

  
  
  
  
  
  
 
