---
layout: post
title:  "Precourse: Check!"
date:   2015-12-15 14:10:01 +0100
categories: makers
---

The course starts full time tomorrow! Yikes! I’m relieved, terrified, and excited at the same time. I’ve got my copy of the Well-grounded Rubyist, my terminal is set up the way I like it, and my laptop is covered in stickers… yep, I’m on my way to becoming a programmer!

Sooo here’s what’s happened since I wrote my last post.

### **Week 1: Command line and Git**

Honestly before I worked with the **command line** I thought developers must be really sad because they miss out on all those beautiful user interfaces us normal people use.

I kinda thought of it as something quaint and outdated kinda like record players or transistor radios.

![Old-fashioned computer](https://makersandlegos.files.wordpress.com/2016/01/giphy-2.gif?w=870&h=870)

**_That’s what I imagined the command line looks like_**

But without realising it, I now use it to open most files, install most things, and even log tasks on it with Taskwarrior! I quickly transitioned from feeling like this:

![Tom Hanks slowly typing](https://makersandlegos.files.wordpress.com/2016/01/bqcxapk.gif?w=730)

**_Terminal.. nah, cmd+space!_**

to this:

![Tony Stark being futuristic](https://makersandlegos.files.wordpress.com/2016/01/giphy.gif?w=730)

**_I am sooo futuristic when I auto-complete file paths_**

As for **github**, it’s amazing! There should be something like this for digital artists… My process always ended up like this: v1, v2, v2-newer, v2-newest, v5, v-final, final version, final-version-edit, FINAL_version, FINAL_version_1…

There’s a lot of problems with this.

* Staying consistent is difficult
* Finding the final version can be challenging
* If you want to branch out in the middle of this stream of versions to experiment it’s near-impossible
* Because of the above issues, deciding to save a separate version becomes a Big Decision that you want to avoid if you’re in the zone
* Avoiding this decision leads to significantly less saves and higher chances to mess up

Github solves a lot of these version control issues. But with art you can at least recognise whether it’s a sketch or a close to finished piece by looking at it for a few seconds. With coding if I relied on that same flawed and lazy system, I would never know which version of anything I’m working on! That’s just one thing that’s impressive about github. There’s plenty more though ^^

### **Weeks 2 & 3 Soo much Ruby**

These weeks were a blur for me. Oh wait, I remember .. something!

![99 bottles of beer on the wall](https://makersandlegos.files.wordpress.com/2016/01/99-bottles.gif?w=549&h=379)

_**Thanks Chris Pine! I’m ruined for life now..**_

Honestly there’s way too many things I learned these two weeks. It would be impossible to summarise all of them, but here are a few of the highlights:

* **Spend your time wisely**. If the instructions say don’t spend more than an hour on something, don’t.. unless you know you are a magical, disciplined individual that knows what they’re doing. I spent way too much time on the exercises I enjoyed (pet dragon) or the ones that I was bent on refactoring (roman numerals).
* **Working full time during this was tough**. I only worked during week 1 & 2, but I felt drained! I was lucky I could sneak in some project work during work hours, but it was still exhausting..At the same time I was almost as productive as the weeks I was off work. I don’t know if this is because I was motivated due to lack of time before or if I was just exhausted by week 3.
* **Meet with people and work together**. The few times I worked with others helped a lot. Especially because people would ask questions that I thought I knew the answer to, but often didn’t.
* **Try and enjoy yourself**, it’s actually pretty fun making things work for their own sake, rather than being fixated on a deadline.

### **Week 4 Will you be my pair-partner?**

This was an interesting week. It was a lot more relaxed than the previous two. I’m kinda glad about that because I’d  had a bad string of flues, so it was good to have some time to chill. I read bits of programming books, watched a few talks (Bojidar Batsov, Sandy Metz, Avdi Grim). But the main focus was on pair-programming and TDD. We were introduced to writing tests in the mighty RSpec.

RSpec is used to write code to test the code you’re planning on writing:)

So let’s say you want to write a simple program that gives you the square of a number. Instead of rushing into a method that does just that, you write an expectation in a test file. Before you write any other code, that’s crucial!

The expectations are simple things like- if I give my non-existing method the number 3 I should receive a 9. Then you run the test, see it fail because your function doesn’t yet exist, and write the simplest possible code to fulfill that expectation. In this case it would be to define a method that returns the number 9 like this:
{% highlight ruby %}
def square
  9
end
{% endhighlight %}

and you keep slowly writing more tests and improving the code until you have something more like this:

{% highlight ruby %}
def square(num)
  num**2
end
{% endhighlight %}

Then once the test passes you write another one and so on. There’s a lot of good reasons for this:

* You don’t make assumptions about the things your code does
* If you refactor you know that the new version will be at least as good as the old one
* You document your code as you’re writing it, rather than make lengthy, incomplete or even outright outdated documentation no-one wants to read
* If you break something there’s a big chance you can pinpoint what you broke
* You gain structure and discipline doing one specific thing at a time

But testing can also feel like this:

![kid doesn't want to hit pinata](https://i0.wp.com/38.media.tumblr.com/538c84f63765a398b291429a55882331/tumblr_inline_n6vkoiTSqe1raprkq.gif)

or like this:

![test doesn't work as expected](https://i2.wp.com/38.media.tumblr.com/c51876c7104492f62b827b1e34f93fab/tumblr_inline_mhagxdlsyz1qz4rgp.gif)

As for pairing – I haven’t had enough practice this week to talk about it in length. But I’ve noticed in my previous jobs that working together with someone on a common problem meant we were focused, having a bit of fun, and usually came up with damn good solutions we wouldn’t have figured out otherwise.

Let’s see what happens tomorrow! :)
