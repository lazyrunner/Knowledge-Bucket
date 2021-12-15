# How to use github for project development

In this tutorial, we will be discussing about how use github as a team for project development. The project at hand is the github page for [printyourbrain](https://printyourbrain.github.io/); so some examples would be specific to rendering pages in github. 
Before we go into the specifics, let us discuss the flow of working as a team with git as version control system. 
The first step that we take as a team is to create the project in github. This is shown in Step 1. What happens in this step is that we create the folder structure to keep our code and other resource files (images etc). This step is done only once per project and is done by a single person (usually the admin). 
Once, the repository is created, each team member clones the repository into their local system (Step 2) so that they can develop in theirconvenience.
An important requirement for contributing in project development is that each member develop in their own specific branch. This is done so that to make sure every person can contribute independently (concurrently). Once a feature or item is developed properly, it is merged into the ```main``` branch with the help of a ```merge request```. This is shown in Step3 - Step 5. Additionally, we discuss some other steps from Step 6 onwards. 


## Author: Sudeshna Bora

---

## Step 1: Create repository 

The first step is to create a repository (or a project) in github. This can be done in two ways, first create the repository in the webpage and second is to create the repository locally and then synchronise/push it to github webpage. 
We would be discussing about Way 1. Information about Way 2 can be found [here](https://kbroman.org/github_tutorial/pages/init.html
)

### Way 1 : Creating repository in the website


```
Step 1: Go to www.github.com 
Step 2: Log into it to go into your homepage.
Step 3: In the upper right corner , there is a + symbol, click on it to see the dropdown menu.
Step 4: In the dropdown menu, you will get the option to create a new repository. Click on it.
```

Once we have clicked on ```create a new repository```, we can select a suitable name, description, privacy status, license if any.
Once this is done a new repository will be created which can be found in your profile. 
For our case, we would name the repository ```<desired_string>.github.io```. This is a stipulation to use github pages (the repository should have .github.io)

---

## Step 2 : Cloning the repository



