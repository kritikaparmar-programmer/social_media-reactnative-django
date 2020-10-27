# Contributing Guidelines
- This is a beginner friendly documentation. Follow the given steps to make a pr and enter in the world of Open Source.

# Steps for Contributing:

### Step 1 - Finding Issue
![issues](https://user-images.githubusercontent.com/59971890/97007288-ce77d100-155e-11eb-808e-eb863c1e4aa7.png)
- Choose an issue suitable to you, the issue must not be assigned to someone else or create your own issue
- Ask from the author of the issue to assign the issue to you and wait until you get assigned

## Step 2 - Fork the Repository
- After you get assigned to an issue the next step is to work on that issue and for that you need to fork the repo.
* NOTE - This step is done only once
- Click the fork button on the repo page
![fork](https://user-images.githubusercontent.com/59971890/97007353-ea7b7280-155e-11eb-80d2-ec2c517b9a8f.png)
![](https://1.bp.blogspot.com/-Mr0ivoTwn9g/UaW9QoSD8zI/AAAAAAAAABw/953TmwhDRhw/s1600/forking-in-progress.png)
- This will create a copy of forked repo in your profile

## Step 3 - Clone the Repository
- After forking run the following commands in git bash 
```
$ cd Desktop
$ git clone https://github.com/<your-username>/<repo-name>
$ cd <repo-name>
$ git remote add upstream https://github.com/<upstream-owner>/<repo-name>
```   
- If you have already forked the project, update your copy before working.
```
$ git remote update
$ git checkout <branch-name>
$ git rebase upstream/<branch-name>
```

## Step 3 - Branch (IMP)
#### NOTE -  There must be a separate branch for each issue!
- Create a new branch, on which you will work 
```
$ git checkout -b branch_name
```

## Step 4 - Git add / commit / push
- After you've made changes or made your contribution to the project add changes to the branch you've just created and commit with a descriptive message of the changes you've made
```
# To add all new files to branch Branch_Name
$ git add .
$ git commit -m 'message'
```
- After this push your work to your remote repository
```
$ git push -u origin Branch_Name
```

## Step 5 : Pull Request
- Go to your forked repository in browser and click on compare and pull requests.
![compare pr](https://user-images.githubusercontent.com/59971890/97012110-26b1d180-1565-11eb-96ee-5928a07fc45d.png)

- Then add a title and description to your pull request that explains your contribution.
![pr](https://user-images.githubusercontent.com/59971890/97012171-35988400-1565-11eb-98bc-0fb397fd6c93.png)
- Then Compare and Pull Request

Easy! Isn't it? So you've submitted your PR. Now wait for any mentor to review and merge your PR.

## Still Confused?
Refer to the following video 
- [Git and Github](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
