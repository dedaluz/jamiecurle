title: "Quick Guide to branching & merging in GIT"
description: "Branching is great idea to develop additional functionality, but whilst still maintaining a stable master branch."
created: 2011-06-21 06:37:27
---

![GIT](http://media.jamiecurle.com/uploads/2011/06/21/blogimage/git.850x600.png)

Branching confused me for a while and I shyed away from it. Now it's my bestest friend in the world, we laugh and play together all day. You didn't come here to read about that though, because you're busy and important and you want to get stuff done. So let's crack on.

## Scenario

[I've made a rather basic project](https://github.com/jamiecurle/branchbasics) that you can clone if your interested in doing that, but all you need to know is that we have a project that is about cats.  Our client is going to change their mind and decide that they want the project to feature dogs as well. This is where we're going to branch, and we'll call that branch "plusdogs". We'll add the changes that incorporate dogs into the plusdogs branch and then merge them back into the master branch, which is where you'll find [the github project](https://github.com/jamiecurle/branchbasics) at


## Cats & Kittens

![Original Project](http://media.jamiecurle.com/uploads/2011/06/21/blogimage/original_2.850x600.jpg)


As you can see, the original project is all about Cats & Kittens, but our client is about to change their mind and decide that they want dogs in on the project  as well.  Let's get busy and bust some "mad branch skillz"

First of all let's list the available branches

<code lang="bash">
git branch -l
</code>

Here's what it came back with, which makes sense because at this point in time there is only the master.

<code lang="bash">
>> * master
</code>


Let's create a the "plusdogs" branch.

<code lang="bash">
git branch plusdogs
</code>

You may think nothing happened because git didn't feedback to you, but it did. Run the list branch command again

<code lang="bash">
git branch -l
</code>

Now you can see the two branches. The Asterix indicates which one you're currently working on. 

<code lang="bash">
>> * master
  plusdogs
</code>

We want to work on the plusdogs branch. To do that we have to check it  out

<code lang="bash">
git checkout plusdogs
</code>

Git will feedback to you telling you that you've switched to the plusdogs branch

<code lang="bash">
>> Switched to branch 'plusdogs'
</code>

## Do The Dog Stuff

So now let's assume that we've been able to complete the work and that our project now looks like this.

![New Project](http://media.jamiecurle.com/uploads/2011/06/21/blogimage/new.850x600.jpg)

We need to add the new files and  commit our changes. 
<code lang="bash">
git add -A
git commit -a -m "Added in the changes for the dog amends"
>> [plusdogs 36cafab] Added in the changes for the dog amends
>> 4 files changed, 295 insertions(+), 867 deletions(-)
>> create mode 100644 img/dog.jpg
>>  rewrite img/kitten.jpg (98%)
</code>

Looks good and now finally push back to the master (on github ) because we want a permanent record of this branch.

<code lang="bash">
git push origin plusdogs
>> Counting objects: 14, done.
>> Delta compression using up to 4 threads.
>> Compressing objects: 100% (7/7), done.
>> Writing objects: 100% (8/8), 176.42 KiB, done.
>> Total 8 (delta 2), reused 0 (delta 0)
>> To git@github.com:jamiecurle/branchbasics.git
>> * [new branch]      plusdogs -> plusdogs
</code>

All is good, we've done our changes, but we still need to merge them into the master branch.


## Merge.

Now all we have to do is merge the changes from our plusdog branch into the master. This bit is easy, but there is something you have to bear in mind and might help to express it as a sentence

> We want to merge the plusdogs branch into the master branch

To do this we have to first switch over to the master branch because we want to merge the changes from plusdogs branch into the master branch.

<code lang="bash">
git checkout master
>>Switched to branch 'master'
</code>

You can see where on the master branch now, but let's double check for that asterix
<code lang="bash">
git branch -l
>>* master
>>  plusdogs
</code>

Looks good, let's merge. The command is very straightforward

<code lang="bash">
git merge plusdogs
</code>

Depending on the size of the merge it'll spit back quite a bit and may even throw a few conflicts at you, but that's outside the scope of this post. Heres what our merge came back with

<code lang="bash">
>>Updating df6df09..36cafab
>>Fast-forward
>> css/global.css |    9 +++++----
>> img/dog.jpg    |  Bin 0 -> 114516 bytes
>> img/kitten.jpg |  Bin 200889 -> 65735 bytes
>> index.html     |   14 +++++++++-----
>> 4 files changed, 14 insertions(+), 9 deletions(-)
>> create mode 100644 img/dog.jpg
</code>

Now all that is left to do is push back to the master

<code lang="bash">
 git push origin master
>>Total 0 (delta 0), reused 0 (delta 0)
>>To git@github.com:jamiecurle/branchbasics.git
>>   df6df09..36cafab  master -> master

</code>

And that's that.

## Conclusion

Branching and merging is an essential part of a professional development process because it enables you to maintain a stable master branch at all times. The only tricky part is to remember that when you merge back from one branch to another __you need to have checked out the branch you want to merge into__ that bit had me stumped for a while.

In my limited experience of merging with subversion, git makes it a pleasure.