---
layout: post
title:  "TDD at Ladies of Code"
date:   2016-08-01 14:11:09 +0100
categories: events
---
Rabea asked me to do a TDD demonstration of a kata, a bit like the ones they do at 8th light. So far I've been lucky to see a few 8th light performances, and these guys really know their stuff!

I've picked Roman Numerals because it has a fairly straightforward problem and solution. I've practiced it with different variations and setups, which led me to figure a few things out for myself.

### **Why Kata practice matters**

Sometimes developers will use katas to practice their coding skills because a kata is a problem, which is typically **well defined** and has a **narrow scope**.

These two characteristics are important for targeted practice. The problem needs to be well-defined so that the requirements are clear and limited up front.

It also needs to have a narrow scope because the goal should be achievable in a few hours (hopefully).

This way you get to know when the kata is done. And for me that's been an issue with pet projects. I find it difficult sometimes to narrow down the focus of the project and limit its features. I get too excited I guess!

 The other benefit is that if they are short enough, you can use them to practice other languages. I've done the same katas in ruby, javascript, clojure, java, and even pony! That doesn't mean I know how to code well in every one of those languages but at least I can read their syntax easier now and have a better feel for how similar, but also different these languages can be!

 But I've not really done the type of practice they do at 8th light where you try the same kata over and over in the same language. For me, I felt, if a problem has been solved well once, then it's solved and that should be good enough. I really couldn't see the benefit of redoing the same kata, because I didn't think of adding extra limitations to it.

 There's code retreats where you pair with a new person each time but you work on the same kata over and over again. Each round has a different requirement that makes it harder - so first you pair with someone on a language you don't know, next you have to write and pass a test every 2 minutes, next you pair silently, etc.

 And because of this demonstration practice, I've had to put some 'limitations' to the kata practice.

 * Time limit - around 15 minutes
 * Readability - others will need to be able to read the code as I write it
 * Process - others will be watching the process and steps, not just the final code

Especially because this is a TDD demonstration the process is key. When I did a practice run at 8th light, the feedback I received was really helpful. While practicing at home I had a step-by-step process that I followed, and I typically managed to stick to it. But when doing the demonstration in front of an audience, speed subconsciously became my priority, which means I didn't develop the algorithm as well as I usually did. I didn't notice that I wasn't pressing my keyboard shortcuts properly, so sometimes the tests weren't running. These are examples of things that aren't a priority if you are just coding for yourself, but all of a sudden become crucial in this new context.

This all may sound like nitpicking, but keeping a proper process is something very valuable - it keeps you accountable. And really an excellent way you can keep yourself consistently accountable is by having someone there with you. I've noticed it with pairing. But with an audience, the pressure is so much higher!

So while practicing for this I've taken a hard look at my process. I haven't improved it to perfection, I think there's a LOT more to work on, but here are some of the things I've tried and kept.


### **Know your tools well**

Shortcuts, snippets, packages are all excellent features of an editor that can help speed up your development. Especially when it comes to a kata, this is pretty useful. I could probably take over 40 min to do the Roman Numerals kata with some dilly-dallying and not using my editor to its full ability. Which is a shame, because I can also do it in 10 min, and it's likely it can be done in 5. Practice becomes so much more annoying when it's time consuming and when it's done mindlessly. But if you are trying to speed your process up, that makes things a bit more engaging! And one of the best ways to code faster and more confidently is to learn your tools. So I've added better snippets, I'm learning atom's shortcuts, and am trying to be more determined when I use my editor. It's taking some practice!

### **Context switching is too much effort**

The first thing I notice when looking at people working with vim is that they know their tools very well. But there's more to it. They keep context switching to a minimum.

* Code is kept in one window, organised in multiple panels
* Tests are run in the same window, in their own panel
* Keyboard shortcuts are preferred over switching between mouse and keys
* Automation is preferred to typing

It's much easier to keep your mind focussed on a complex design if you don't have to keep switching from one window to another, looking for files or tests. If the tests can run automatically on save, even better! Cedric recommended [Guard](https://github.com/guard/guard) to me for that.


### **Keep an eye on the mistakes you make**

Each time I practiced the kata I discovered a new mistake developing. During one try I was using ctrl + s instead of cmd + s to save, even though I've been using a Macbook for well over a year now. Another time I wrote "if number = 0" instead of "if number == 0". And so on..

I found it hard to keep track of mistakes I made because I like to think I don't make silly mistakes. :)

Noting your typical mistakes helps prevent them from turning into habits. It also shows you where you need more work to be more comfortable with your tools or language.

## **Try new things out**

A big benefit of kata practice has been finding out new unexpected ways to do things. Once you've done the same kata enough times, you'll probably get a bit bored! And you might not want to try out too many new things in big projects, but I think experimenting with different kata solutions is great for learning.

Roman Numerals has been done over and over and there are so many resources out there. There's a lot of different solutions, some more popular/famous than others.

[Corey Haines's narrated video](https://www.youtube.com/watch?v=vX-Yym7166Y#t=53) is one of the first ones I've found and seems to be a typical approach, though Enrique was very much against doing the tests this way.
[Scott W from F Sharp For Fun and Profit](https://fsharpforfunandprofit.com/posts/roman-numeral-kata/) - has a very unusual approach, and it's where I learned about property testing for the first time. I especially liked this blog post because it was written in direct response to the video by Corey Haines above. Scott points out several things that bothered me about Corey's solution too! The use of a random magic number in the test to 'prove' that the final algorithm works is not reliable when we're solving an unknown problem, whose solution we can't 'just know' is correct.

So I've been using Rantly for property testing with RSpec, trying to combine it with unit testing, to see a mixed approach between Corey's and Scott's. Rantly doesn't seem to be widely used, even though it was created in 2013. It's not a new concept though, Haskell has an excellent library, called QuickCheck, Scala has ScalaCheck, etc.

The idea is simple: there are properties of your methods and their output that should always be true, not matter what. In the case of roman numerals some properties include:

* There should never a IIII - because IIII should be IV
* Similarly there should never be a XXXX, instead the result for 40 should be XL
* Though there might be 4 X in the program like for 39 - XXXIX, they should never be 4 in a roll, but there can never be 4 I ever, even if not in a roll
* There should only ever be one IV, V, VI, IX, XI etc.

Once you know your domain well, you can come up with these rules and the library will create random numbers for you and run multiple tests against each property. One thing Rantly does well is it shrinks the number to the smallest one that breaks your test. This makes it easier to find what is missing in your program, because it's not just any random number. The tests will continue to break consistently because of the same reason.

Here's an example property test using Rantly

```
require ‘rantly/rspec_extensions'

 it "can never have a XXXX” do

    property_of { Rantly {
      call ([:range, 0, 100])}
    }.check {|integer|
      roman = roman_numerals.arabic_to_roman(integer)
      number_of_XXXX = roman.scan("XXXX").count
      expect(number_of_XXXX == 0).to be_truthy
    }

  end
```

And here's the code for Roman Numerals

```
class RomanNumerals

  CONVERSIONS = {
    10 => "X",
    9 => "IX",
    5 => "V",
    4 => "IV",
    1 => "I"
  }

  def arabic_to_roman(number)
    return "" if number == 0
    arabic, roman = CONVERSIONS.select {|arabic, roman| arabic <= number}.first
    roman + arabic_to_roman(number - arabic)
  end
end
```
Say I only have a solution implementing 1-10 ("I" to "X"), like the one above. Now let's say I want the code to work from 0 to 100. The current code would work up to 39, but I may not know that. Perhaps my codebase is too complicated or big or I don't even know the codebase. All current unit tests are passing. But I can't see the limitation.

If I know certain facts that should always be right I can now test for those! I find this to be magical :)

Give property testing a try at least, I've been really impressed with what it can do!
