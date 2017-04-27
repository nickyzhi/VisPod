# -*- coding: utf-8 -*-

import json
import sys

with open('dataset.json', 'w') as output:
    data = [{},{},{},{},{},{}]
    data[0]["topicName"]= "Opening & AD"
    data[0]["topicDuration"]= "280"
    data[0]["startTime"] = "00:00:00"
    data[0]["events"] = [{}]
    data[0]["events"][0]["eventTime"] = "00:01:36"
    data[0]["events"][0]["eventName"] = "AD: onnit.com/model for 10% OFF"
    data[0]["sentences"] = [{
            "sentenceTime": "00:00:00",
            "sentenceContent": "This podcast of The Model Health Show is presented",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:00:03",
            "sentenceContent": "to you by Shawn Stevenson with Rare Gem Productions.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:00:06",
            "sentenceContent": "For more information visit theshawnstevensonmodel.com.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:00:14",
            "sentenceContent": "Welcome to The Model Health Show, this is fitness and nutrition expert,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:18",
            "sentenceContent": "Shawn Stevenson, here with my cohost and producer,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:20",
            "sentenceContent": "the amazing Jade Harrell. What's up Jade?",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:23",
            "sentenceContent": "What's up Shawn?",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:00:25",
            "sentenceContent": "How are you doing today?",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:26",
            "sentenceContent": "Man, what an intro you just made. I am fantastonishing!",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:00:31",
            "sentenceContent": "Fantastonishing? Break that down for me, what is that?",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:35",
            "sentenceContent": "Fantastically astonishing or astonishingly fantastic.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:39",
            "sentenceContent": "Either way, I like it. It's like the reversible cap.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:43",
            "sentenceContent": "You get two different styles in one cap. Awesome, awesome.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:48",
            "sentenceContent": "Well, glad to hear that. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:49",
            "sentenceContent": "And everybody, thank you so much for tuning in.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:50",
            "sentenceContent": "We've got an amazing show for you today.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:53",
            "sentenceContent": "Today we're going to be talking about how to boost your sex hormones.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:00:56",
            "sentenceContent": "Well, we'll take that.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:00:57",
            "sentenceContent": "In particular, we're going to be talking about how to boost testosterone naturally.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:01",
            "sentenceContent": "Testosterone is important for men and women.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:03",
            "sentenceContent": "I was just going to say, is this for the guys today?",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:01:06",
            "sentenceContent": "Yeah, it's a far deeper thing than just about sex.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:10",
            "sentenceContent": "It's really about a lot of other important ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:13",
            "sentenceContent": "and fundamental things for us to be healthy and fit long term. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:17",
            "sentenceContent": "Testosterone is a big player in that so we're going to talk all about that. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:19",
            "sentenceContent": "I'm also going to be wrapping the show up ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:20",
            "sentenceContent": "by sharing with you ten ways to boost your testosterone naturally.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:24",
            "sentenceContent": "Okay.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:01:25",
            "sentenceContent": "And many of these things are the price of free. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:28",
            "sentenceContent": "You know, my favorite price. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:31",
            "sentenceContent": "So, stay tuned for that ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:32",
            "sentenceContent": "but first let's give a shout out to our show sponsor, onnit.com.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:36",
            "sentenceContent": "Head over to onnit.com/model for 10% all your health and human performance supplements.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:46",
            "sentenceContent": "If you don't know by now you've got to get the Hemp FORCE.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:50",
            "sentenceContent": "Hemp protein is the most bioavailable protein for the human body.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:53",
            "sentenceContent": "If you're going to be somebody who's operating at a high level,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:56",
            "sentenceContent": "working out, getting your train on, getting your body together, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:01:59",
            "sentenceContent": "you need some high-quality protein and hemp is the way to go. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:03",
            "sentenceContent": "You are not going to be dealing with all the nefarious, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:06",
            "sentenceContent": "kind of sketchy stuff as you move up the food chain.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:09",
            "sentenceContent": "You're dealing with, what did that cow eat that I'm drinking. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:11",
            "sentenceContent": "Of course, if you get whey protein it's going to be from 5,000 cows.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:15",
            "sentenceContent": "And I'm just saying, they are not keeping food diaries, okay.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:02:19",
            "sentenceContent": "Exactly. So all of those immunological factors can potentially ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:24",
            "sentenceContent": "cause an autoimmune response in your body. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:26",
            "sentenceContent": "I'm not saying that for all whey proteins ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:27",
            "sentenceContent": "but the standard stuff out there ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:29",
            "sentenceContent": "is not the best so we're going to cut away that whole pathway ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:33",
            "sentenceContent": "and get onto something of a higher quality, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:35",
            "sentenceContent": "that good plant-based protein so you're not going to be worrying about",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:38",
            "sentenceContent": "toxins working their way up the food chain.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:41",
            "sentenceContent": "It will be lower toxicity. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:43",
            "sentenceContent": "Also, it's organic too so you're not dealing with pesticides, fungicides. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:46",
            "sentenceContent": "It's estrogenic compounds, by the way, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:49",
            "sentenceContent": "since we're talking about building testosterone.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:52",
            "sentenceContent": "These things, when you're dealing with pesticides can actually hurt your test. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:56",
            "sentenceContent": "So we're going to call testosterone,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:57",
            "sentenceContent": "we're going to shorten it today and call it test.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:02:59",
            "sentenceContent": "Test, we're going to call it test.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:03:01",
            "sentenceContent": "So definitely get your hands on some Hemp FORCE protein. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:04",
            "sentenceContent": "We love the vanilla acai and the choco maca.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:06",
            "sentenceContent": "Both flavors are incredible.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:07",
            "sentenceContent": "Yes they are.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:09",
            "sentenceContent": "Also, the SHROOM Tech. That's a pre-workout. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:12",
            "sentenceContent": "Or, as Jade says, a pre- life. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:13",
            "sentenceContent": "It gets your energy right, nice, natural consistent energy. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:17",
            "sentenceContent": "You're not going to be spiked out like Spike Lee trying to trip referees, you know. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:22",
            "sentenceContent": "You're going to feel good and consistent. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:24",
            "sentenceContent": "And it is coming from something that's got 5,000 years of documented history ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:27",
            "sentenceContent": "in Chinese medicine so it's been around a while.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:30",
            "sentenceContent": "I love it.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:03:31",
            "sentenceContent": "Also, with the news clinical studies today showing its impact ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:34",
            "sentenceContent": "on oxygenating your blood, boosting stamina, improving your insulin sensitivity ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:39",
            "sentenceContent": "which means less belly fat, it's really powerful stuff. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:42",
            "sentenceContent": "We're talking about cordyceps mushroom ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:44",
            "sentenceContent": "and that's the basis of the SHROOM Tech formula so those are two incredible things.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:48",
            "sentenceContent": "They've got a lot more so head over there ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:49",
            "sentenceContent": "and check them out, onnit.com/model for 10% off.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:53",
            "sentenceContent": "Now let's get into the iTunes review of the week",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:55",
            "sentenceContent": "Here's a five-star rating Shawn which we so love to receive. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:03:59",
            "sentenceContent": "It says, 'Awesome podcast. One of the best.' From Howard H.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:04",
            "sentenceContent": "'I heard an interview of Shawn on the Smart Passive Income podcast.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:07",
            "sentenceContent": "I was so glad I started listening. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:09",
            "sentenceContent": "I bought his Sleep Smarter book twice, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:11",
            "sentenceContent": "one for me and the other for my daughter.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:14",
            "sentenceContent": "I've been enjoying his podcast from the first one. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:17",
            "sentenceContent": "There is so much good information that I can't stop listening.'",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:21",
            "sentenceContent": "Wow, that is incredible.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:22",
            "sentenceContent": "That worked.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:04:23",
            "sentenceContent": "That's incredible. Spreading the love.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:24",
            "sentenceContent": "Yes.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:04:25",
            "sentenceContent": "The LUV. I love it. Thank you so much. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:28",
            "sentenceContent": "Thank you so much for leaving that review ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:29",
            "sentenceContent": "and everybody thanks for heading over to iTunes ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:31",
            "sentenceContent": "and leaving reviews for the show. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:33",
            "sentenceContent": "That means so much. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:35",
            "sentenceContent": "It makes my day every single time I open those up ",
            "sentenceSpeaker": "shawn"
        }]
    data[0]["keywords"] = [{},{},{},{},{},{}]
    data[0]["keywords"][0]["keywordScore"] = "9"
    data[0]["keywords"][0]["keyword"] = "onnit.com"
    data[0]["keywords"][1]["keywordScore"] = "3"
    data[0]["keywords"][1]["keyword"] = "10% off"
    data[0]["keywords"][2]["keywordScore"] = "9"
    data[0]["keywords"][2]["keyword"] = "Testosterone"
    data[0]["keywords"][3]["keywordScore"] = "5"
    data[0]["keywords"][3]["keyword"] = "audience"
    data[0]["keywords"][4]["keywordScore"] = "9"
    data[0]["keywords"][4]["keyword"] = "reviews"
    data[0]["keywords"][5]["keywordScore"] = "10"
    data[0]["keywords"][5]["keyword"] = "Opening & AD"


    data[1]["topicName"]= "What is Testosterone"
    data[1]["topicDuration"]= "192"
    data[1]["startTime"] = "00:04:40"
    data[1]["events"] = [{}]
    data[1]["events"][0]["eventTime"] = "00:05:25"
    data[1]["events"][0]["eventName"] = "Testosterone Decide Gender? How??!!"

    data[1]["sentences"]=[{
            "sentenceTime": "00:04:40",
            "sentenceContent": "we’re going to talk about what is testosterone in the first place.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:43",
            "sentenceContent": "We’ve got to define it. And if it’s such a widespread problem, this is…we need to know.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:04:49",
            "sentenceContent": "So testosterone is essentially a steroid hormone.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:52",
            "sentenceContent": "It’s part of an androgen group. The androgen groups are essentially",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:04:57",
            "sentenceContent": "known as the male hormones. This is what makes men more masculine and ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:01",
            "sentenceContent": "also helps to facilitate a lot of other functions in females as well.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:06",
            "sentenceContent": "Testosterone is secreted primarily by the testicles of males and the ovaries of females.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:12",
            "sentenceContent": "But a small amount is secreted from the adrenal glands as well. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:16",
            "sentenceContent": "Okay, so now that we’ve gotten a little bit of a definition let’s talk about what testosterone does.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:20",
            "sentenceContent": "So, testosterone really, the most important, fundamental thing is that before birth ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:25",
            "sentenceContent": "it determines whether or not a baby will develop into a boy or a girl.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:28",
            "sentenceContent": "How about that.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:05:30",
            "sentenceContent": "Now a lot of people don’t realize this but we all start off as girls. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:36",
            "sentenceContent": "We all start off in the womb…",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:37",
            "sentenceContent": "Who runs the world, girls, who runs the world, girls.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:05:39",
            "sentenceContent": "Cue Beyoncé. We all start off in the womb with the female template.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:43",
            "sentenceContent": "How about that.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:05:45",
            "sentenceContent": "So basically, after the egg gets fertilized, the sperm and egg meet,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:48",
            "sentenceContent": "there are different phases, the zygote, fetus, and this whole thing. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:51",
            "sentenceContent": "But there comes a point where there’s a big shed of testosterone ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:05:55",
            "sentenceContent": "from the mother to the fetus that results in the dropping down of the testicles. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:00",
            "sentenceContent": "Basically, for women, the ovaries kind of stay up there. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:03",
            "sentenceContent": "For guys, they drop down and become the testicles.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:06",
            "sentenceContent": "That is so amazing.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:06:07",
            "sentenceContent": "Isn’t that crazy?",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:08",
            "sentenceContent": "It is crazy. So they’re the same thing, just an innie and an outie.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:06:12",
            "sentenceContent": "Exactly! And one of them is more dangerous. Out in the world you’ve got ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:16",
            "sentenceContent": "to protect them. It’s a whole different ballgame.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:18",
            "sentenceContent": "Which goes back to that valuable womb.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:06:21",
            "sentenceContent": "And also, this is the sprouting or the birth of the penis as well due to that. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:25",
            "sentenceContent": "And, of course, the different chromosome is determined by the father ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:30",
            "sentenceContent": "but the testosterone level in the mother is also important in how",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:33",
            "sentenceContent": "big these things get or how much testosterone the baby is going to have.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:37",
            "sentenceContent": "So it all kind of sets your template early in life as to what your genetic",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:41",
            "sentenceContent": "disposition is going to be. However, with that said, genes only play a ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:44",
            "sentenceContent": "certain percentage of the role in your testosterone because you have a lot",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:48",
            "sentenceContent": "of influence in your testosterone levels in what you do in your day to day life.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:53",
            "sentenceContent": "Just to make that kind of short and sweet and to end it right there ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:55",
            "sentenceContent": "because we could talk about that the entire show, is that",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:06:58",
            "sentenceContent": "testosterone is literally what makes you a male when you’re developing.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:00",
            "sentenceContent": "Sure, but then it continues to be an influence throughout your lifetime,",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:07:05",
            "sentenceContent": "that we have some more control over.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:07:07",
            "sentenceContent": "Exactly. And in adult males, their level of testosterone is about ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:11",
            "sentenceContent": "seven to eight times greater than adult females.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:14",
            "sentenceContent": "Really?",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:07:15",
            "sentenceContent": "Now there are different degrees of that depending on where they are ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:19",
            "sentenceContent": "in the day, depending on a lot of different factors, because it can ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:23",
            "sentenceContent": "be as great as 20 times as much. But still, I want to make the point",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:26",
            "sentenceContent": "that women have testosterone too and it’s very, very important ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:30",
            "sentenceContent": "for your health and longevity.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:31",
            "sentenceContent": "So testosterone is also important regulating the sex drive in men and women. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:36",
            "sentenceContent": "It’s important for starting and maintaining the development of male sex ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:40",
            "sentenceContent": "characteristics including emotional and physical strength, the body shape,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:44",
            "sentenceContent": "hairiness, deepness of the voice, and even the way you smell, your odor. Odor.",
            "sentenceSpeaker": "shawn"
        }]


    data[1]["keywords"] = [{},{},{},{},{},{}]
    data[1]["keywords"][0]["keywordScore"] = "4"
    data[1]["keywords"][0]["keyword"] = "fundamental"
    data[1]["keywords"][1]["keywordScore"] = "8"
    data[1]["keywords"][1]["keyword"] = "hormone"
    data[1]["keywords"][2]["keywordScore"] = "5"
    data[1]["keywords"][2]["keyword"] = "genetic"
    data[1]["keywords"][3]["keywordScore"] = "7"
    data[1]["keywords"][3]["keyword"] = "health"
    data[1]["keywords"][4]["keywordScore"] = "3"
    data[1]["keywords"][4]["keyword"] = "sex"
    data[1]["keywords"][5]["keywordScore"] = "10"
    data[1]["keywords"][5]["keyword"] = "Testosterone"

    data[2]["topicName"]= "Testosterone Impact"
    data[2]["topicDuration"]= "98"
    data[2]["startTime"] = "00:07:52"
    data[2]["events"] = [{}]
    data[2]["events"][0]["eventTime"] = "00:08:03"
    data[2]["events"][0]["eventName"] = "developing creativity"

    data[2]["sentences"]=[{
            "sentenceTime": "00:07:52",
            "sentenceContent": "It also governs sperm production and quality. It governs your",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:55",
            "sentenceContent": "ability to perform during sexual intercourse. Testosterone also",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:07:59",
            "sentenceContent": "plays a role in developing your creativity, intellect, and by the way,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:03",
            "sentenceContent": "this is all backed by clinical studies. So it has a role in developing",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:07",
            "sentenceContent": "your creativity, your intellect, your thought patterns, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:10",
            "sentenceContent": "your drive, your assertiveness. We all know this, men and women,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:14",
            "sentenceContent": "as well as the ability to propose new ideas and to carry them out to",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:19",
            "sentenceContent": "their conclusion. So that’s that quality of drive. Are you a driver?",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:24",
            "sentenceContent": "Testosterone does play a role in that because you can only talk yourself",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:28",
            "sentenceContent": "up so much. But are you following through? ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:30",
            "sentenceContent": "Your testosterone levels could be an influencing player in that.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:34",
            "sentenceContent": "That’s very interesting. High five to testosterone for all that.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:08:38",
            "sentenceContent": "Right. Also, testosterone plays a role in bone maturation and bone density.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:43",
            "sentenceContent": "Also, your muscle mass. This is captain obvious here",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:45",
            "sentenceContent": "A lot of people know that one. Protein synthesis.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:48",
            "sentenceContent": "So your body actually building things, breaking down proteins and making it",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:52",
            "sentenceContent": "into other stuff. That is so critical. You are a protein being. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:55",
            "sentenceContent": "Testosterone plays a role in this.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:08:57",
            "sentenceContent": "It is also a regulator of cognitive and physical energy. So, like your",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:01",
            "sentenceContent": "brain health. We’re also going to talk about some of the negative things",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:03",
            "sentenceContent": "if you don’t have optimal testosterone levels. Testosterone is also responsible",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:08",
            "sentenceContent": "for acute stress response. So, how are you under stress.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:11",
            "sentenceContent": "How are you reacting? Are you going to be more driven to get things done,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:15",
            "sentenceContent": "to accomplish that goal even when stress shows up,or are you going to retreat?",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:19",
            "sentenceContent": "Your testosterone does have a huge impact on that.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:23",
            "sentenceContent": "So now that you know a little bit about what testosterone does in your",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:26",
            "sentenceContent": "body and in your friends’ body, your partner, mother, father, brother,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:31",
            "sentenceContent": "everybody that you know, it’s impacting them. Now that you understand a little",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:34",
            "sentenceContent": "bit about what it does I’m going to share with you the process of how",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:38",
            "sentenceContent": "it’s actually created. Now you’ve got to get your science pants on. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:41",
            "sentenceContent": "Get your pocket protector. No, we’re not going to make it too complicated.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:44",
            "sentenceContent": "But I am going to take you through the biochemical process here.",
            "sentenceSpeaker": "shawn"
        }]


    data[2]["keywords"] = [{},{},{},{},{},{},{}]
    data[2]["keywords"][0]["keywordScore"] = "8"
    data[2]["keywords"][0]["keyword"] = "creativity"
    data[2]["keywords"][1]["keywordScore"] = "8"
    data[2]["keywords"][1]["keyword"] = "intellect"
    data[2]["keywords"][2]["keywordScore"] = "8"
    data[2]["keywords"][2]["keyword"] = "cognitive"
    data[2]["keywords"][3]["keywordScore"] = "8"
    data[2]["keywords"][3]["keyword"] = "physical energy"
    data[2]["keywords"][4]["keywordScore"] = "4"
    data[2]["keywords"][4]["keyword"] = "nbiochemical"
    data[2]["keywords"][5]["keywordScore"] = "9"
    data[2]["keywords"][5]["keyword"] = "testosterone"
    data[2]["keywords"][6]["keywordScore"] = "10"
    data[2]["keywords"][6]["keyword"] = "Impact"

    data[3]["topicName"]= "Low Testosterone Impact"
    data[3]["topicDuration"]= "68"
    data[3]["startTime"] = "00:09:46"
    data[3]["events"] = [{}]
    data[3]["events"][0]["eventTime"] = "00:10:01"
    data[3]["events"][0]["eventName"] = "heart disease"
    data[3]["sentences"] = [{
            "sentenceTime": "00:09:46",
            "sentenceContent": "Now here’s what low testosterone can mean for your. According to ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:48",
            "sentenceContent": "clinical studies, men whose testosterone levels are slightly above",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:51",
            "sentenceContent": "average are less likely to have high blood pressure, less likely",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:55",
            "sentenceContent": "to experience a heart attack, and less likely to be obese.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:09:58",
            "sentenceContent": "Give that man some testosterone then.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:10:01",
            "sentenceContent": "Low testosterone means increased heart disease, increased osteoporosis,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:07",
            "sentenceContent": "diabetes, brain aging. This is seen in the research, accelerated",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:13",
            "sentenceContent": "brain aging form low testosterone, and shorter life span. Now, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:18",
            "sentenceContent": "infertility and poor reproductive health also mean more belly fat and",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:22",
            "sentenceContent": "total body fat compared to your lean muscle mass, less muscle growth from the",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:26",
            "sentenceContent": "strength training you’re doing. So, if you’re out there busting it and working out",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:30",
            "sentenceContent": "and training and not really getting the results it might be something to consider",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:34",
            "sentenceContent": "that your testosterone might be low.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:36",
            "sentenceContent": "Also, obviously, poorer athletic performance. So, your athletic performance",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:40",
            "sentenceContent": "will suffer because you don’t have that drive, you don’t have that extra gear.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:43",
            "sentenceContent": "You also have slower recovery from your intense training. And, the headline here",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:48",
            "sentenceContent": "is that you’ll have a greater risk of cancer when testosterone levels are low.",
            "sentenceSpeaker": "shawn"
        }]
    data[3]["keywords"] = [{},{},{},{},{}]
    data[3]["keywords"][0]["keywordScore"] = "8"
    data[3]["keywords"][0]["keyword"] = "blood pressure"
    data[3]["keywords"][1]["keywordScore"] = "8"
    data[3]["keywords"][1]["keyword"] = "obese"
    data[3]["keywords"][2]["keywordScore"] = "8"
    data[3]["keywords"][2]["keyword"] = "osteoporosis"
    data[3]["keywords"][3]["keywordScore"] = "5"
    data[3]["keywords"][3]["keyword"] = "athletic"
    data[3]["keywords"][4]["keywordScore"] = "10"
    data[3]["keywords"][4]["keyword"] = "testosterone"

    data[4]["topicName"]= "Lowering testosterone"
    data[4]["topicDuration"]= "170"
    data[4]["startTime"] = "00:10:54"
    data[4]["events"] = [{},{}]
    data[4]["events"][0]["eventTime"] = "00:10:57"
    data[4]["events"][0]["eventName"] = "First thing to lower"
    data[4]["events"][1]["eventTime"] = "00:12:45"
    data[4]["events"][1]["eventName"] = "Second thing to lower"
    data[4]["sentences"] = [{
            "sentenceTime": "00:10:54",
            "sentenceContent": "So，let’s talk about some of the things that can lower the testosterone.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:10:57",
            "sentenceContent": "First, we’ll start with some of the obvious stuff. The testosterone",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:00",
            "sentenceContent": "can be damaged, especially leydig cells, during sports or other physical trauma.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:07",
            "sentenceContent": "So, if any guy out there, which pretty much all of us have had that ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:11",
            "sentenceContent": "experience of getting nailed in the balls and it’s like...",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:15",
            "sentenceContent": "Does it really hurt like that? I mean, it hurts like that?",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:11:19",
            "sentenceContent": "It feels like somebody is choking you out. It’s so crazy",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:22",
            "sentenceContent": "how it’s connected. It’s pretty bad.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:25",
            "sentenceContent": "Well, if the testicles are...You are doing the hands like....",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:31",
            "sentenceContent": "Maybe I should change the shape. Well, if the testicles are similar to our",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:11:38",
            "sentenceContent": "ovaries except that yours are exposed to dangerous environmental factors",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:11:44",
            "sentenceContent": "and trauma then the only thing I can equate the pain that",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:11:48",
            "sentenceContent": "you are describing to is maybe our monthly cramping that happens.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:11:52",
            "sentenceContent": "You know, the thing is, if you look into this you really can’t find a comparison.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:11:56",
            "sentenceContent": "There’s not, huh? Men are from Mars, women are from Venus?",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:11:59",
            "sentenceContent": "Right. We will never really understand, because we have not gone through it.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:04",
            "sentenceContent": "Sure",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:12:05",
            "sentenceContent": "And you guys can’t really understand what it’s like for us as well.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:06",
            "sentenceContent": "And there’s no language to...",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:12:07",
            "sentenceContent": "Nobody’s pain is more important.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:11",
            "sentenceContent": "No, no-no-no. Who would even bring up childbirth and all that stuff.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:12:16",
            "sentenceContent": "We wouldn’t even go there.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:12:18",
            "sentenceContent": "Let’s not get into a debate.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:19",
            "sentenceContent": "There’s no need.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:12:20",
            "sentenceContent": "So I want people to understand that physical trauma can definitely ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:24",
            "sentenceContent": "hinder your testosterone level production for sure.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:26",
            "sentenceContent": "So, kids out there who are playing sports, collegiate sports, professional",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:30",
            "sentenceContent": "athletes, we’ve got some professional athletes who listen to the show, ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:33",
            "sentenceContent": "make sure that you wear the protection, okay. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:36",
            "sentenceContent": "Jade just tapped a cup. It was a Styrofoam cup. I don’t know",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:40",
            "sentenceContent": "where that came from. But, anyway, protect yourself.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:44",
            "sentenceContent": "Yes, protect yourself.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:12:45",
            "sentenceContent": "Also, radiation treatment or chemotherapy has been shown, clinically proven,",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:49",
            "sentenceContent": "to have negative effects on the leydig cells. There we ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:52",
            "sentenceContent": "are again about the leydig cells. Vasectomy may damage the leydig cells and",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:12:57",
            "sentenceContent": "lead to early andropause and low testosterone levels. Several studies have shown",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:02",
            "sentenceContent": "this. So you’ve got to be careful when we’re making that decision about",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:05",
            "sentenceContent": "getting the vasectomy, getting the little clippie clippie so we don’t have",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:09",
            "sentenceContent": "any more babies, because you could be potentially lowering your testosterone levels.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:13",
            "sentenceContent": "Right, try another way.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:13:14",
            "sentenceContent": "Yeah. We’ve actually talked about some natural birth control methods",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:19",
            "sentenceContent": "on the show with Sara Gottfried.	",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:21",
            "sentenceContent": "We did.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:13:22",
            "sentenceContent": "But this is again, understanding we want to things as natural as possible.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:27",
            "sentenceContent": "Surgery should be far down the line as an option for you because ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:32",
            "sentenceContent": "every surgery is a traumatic even for the human body.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:35",
            "sentenceContent": "Your body is not designed to be cut into so just understand that.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:39",
            "sentenceContent": "We are finding more and more just how much trauma affects our well being.",
            "sentenceSpeaker": "Jade"
        }]
    data[4]["keywords"] = [{},{},{},{},{},{}]
    data[4]["keywords"][0]["keywordScore"] = "8"
    data[4]["keywords"][0]["keyword"] = "physical"
    data[4]["keywords"][1]["keywordScore"] = "8"
    data[4]["keywords"][1]["keyword"] = "testicles"
    data[4]["keywords"][2]["keywordScore"] = "8"
    data[4]["keywords"][2]["keyword"] = "protect"
    data[4]["keywords"][3]["keywordScore"] = "8"
    data[4]["keywords"][3]["keyword"] = "radiation"
    data[4]["keywords"][4]["keywordScore"] = "6"
    data[4]["keywords"][4]["keyword"] = "Vasectomy"
    data[4]["keywords"][5]["keywordScore"] = "10"
    data[4]["keywords"][5]["keyword"] = "Lower"

    data[5]["topicName"]= "Boost Testosterone"
    data[5]["topicDuration"]= "87"
    data[5]["startTime"] = "00:13:44"
    data[5]["events"] = [{},{},{}]
    data[5]["events"][0]["eventTime"] = "00:13:52"
    data[5]["events"][0]["eventName"] = "sunlight"
    data[5]["events"][1]["eventTime"] = "00:14:06"
    data[5]["events"][1]["eventName"] = "lift heavy"
    data[5]["events"][1]["eventTime"] = "00:14:42"
    data[5]["events"][1]["eventName"] = "sex"
    data[5]["sentences"] = [{
            "sentenceTime": "00:13:44",
            "sentenceContent": "Yeah, If you’ve got neighbors who it’s not going to really work for that’s ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:48",
            "sentenceContent": "something you’ve got to consider maybe doing a different way but",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:52",
            "sentenceContent": "I’m just giving you the data here. Sunlight on the testicles directly",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:55",
            "sentenceContent": "can boost your testosterone even more so than getting it on ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:13:59",
            "sentenceContent": "your other body parts.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:00",
            "sentenceContent": "So let the sunshine in. ",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:14:03",
            "sentenceContent": "That’s tip number one to naturally boost your testosterone, get",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:06",
            "sentenceContent": "more sunlight. Tip number two is to lift heavy weights.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:10",
            "sentenceContent": "This is the well-known one. This is known across the board ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:12",
            "sentenceContent": "so we’re not going to spend a lot of time here, but heavy lifts. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:14",
            "sentenceContent": "We’re talking about doing heavy lifting here. So, especially",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:18",
            "sentenceContent": "the compound lifts, the dead lifts, the squats, overhead press, bench press.",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:23",
            "sentenceContent": "These are going to trigger your body to secrete the most anabolic hormones. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:27",
            "sentenceContent": "So these lifts are critical to secreting testosterone. So the dead lift",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:33",
            "sentenceContent": "the squats, bench press, and overhead press, and anything that you’re",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:37",
            "sentenceContent": "putting a heavy load on your body., so this is gonna be the thing...",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:42",
            "sentenceContent": "Number three on our ten ways to naturally boost testosterone is sex. ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:47",
            "sentenceContent": "There you go.",
            "sentenceSpeaker": "Jade"
        },{
            "sentenceTime": "00:14:48",
            "sentenceContent": "Orgasm does not actually affect testosterone levels in the blood in",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:53",
            "sentenceContent": "an acute sense. So, just the short-term secretion, because ",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:14:58",
            "sentenceContent": "a lot of guys are actually concerned that there is a lot of information",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:15:01",
            "sentenceContent": "out there, even movies saying you can’t do it when you are training for",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:15:05",
            "sentenceContent": "your event because you are going to depress your drive because our drive is",
            "sentenceSpeaker": "shawn"
        },{
            "sentenceTime": "00:15:09",
            "sentenceContent": "related to our testosterone. But there is not really much data to back that up.",
            "sentenceSpeaker": "shawn"
        }]
    data[5]["keywords"] = [{},{},{},{},{}]
    data[5]["keywords"][0]["keywordScore"] = "8"
    data[5]["keywords"][0]["keyword"] = "sunlight"
    data[5]["keywords"][1]["keywordScore"] = "8"
    data[5]["keywords"][1]["keyword"] = "lifting"
    data[5]["keywords"][2]["keywordScore"] = "8"
    data[5]["keywords"][2]["keyword"] = "sex"
    data[5]["keywords"][3]["keywordScore"] = "6"
    data[5]["keywords"][3]["keyword"] = "Orgasm"
    data[5]["keywords"][4]["keywordScore"] = "10"
    data[5]["keywords"][4]["keyword"] = "boost"

    

    
    
    #delete '\u0080\u009d, \u0080\u0099

    json.dump(data, output)