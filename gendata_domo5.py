# -*- coding: utf-8 -*-

import json
import sys

with open('dataset.json', 'w') as output:
    data = [{},{},{},{},{}]
    data[0]["topicName"]= "Opening"
    data[0]["topicDuration"]= "14"
    data[0]["startTime"] = "00:00:00"
    data[0]["events"] = [{}]
    data[0]["events"][0]["eventTime"] = "00:00:06"
    data[0]["events"][0]["eventName"] = "Introducing Website"
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
        }]
    data[0]["keywords"] = [{},{},{},{},{}]
    data[0]["keywords"][0]["keywordScore"] = "5"
    data[0]["keywords"][0]["keyword"] = "Shawn"
    data[0]["keywords"][1]["keywordScore"] = "3"
    data[0]["keywords"][1]["keyword"] = "visit"
    data[0]["keywords"][2]["keywordScore"] = "9"
    data[0]["keywords"][2]["keyword"] = "Podcast"
    data[0]["keywords"][3]["keywordScore"] = "5"
    data[0]["keywords"][3]["keyword"] = "Production"
    data[0]["keywords"][4]["keywordScore"] = "10"
    data[0]["keywords"][4]["keyword"] = "Opening"


    data[1]["topicName"]= "Greeting"
    data[1]["topicDuration"]= "34"
    data[1]["startTime"] = "00:00:14"
    data[1]["events"] = [{}]
    data[1]["events"][0]["eventTime"] = "00:00:26"
    data[1]["events"][0]["eventName"] = "Fantastonishing"

    data[1]["sentences"]=[{
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
        }]


    data[1]["keywords"] = [{},{},{},{},{},{}]
    data[1]["keywords"][0]["keywordScore"] = "8"
    data[1]["keywords"][0]["keyword"] = "Hi"
    data[1]["keywords"][1]["keywordScore"] = "8"
    data[1]["keywords"][1]["keyword"] = "Fantastonishing"
    data[1]["keywords"][2]["keywordScore"] = "5"
    data[1]["keywords"][2]["keyword"] = "Awesome"
    data[1]["keywords"][3]["keywordScore"] = "3"
    data[1]["keywords"][3]["keyword"] = "How"
    data[1]["keywords"][4]["keywordScore"] = "3"
    data[1]["keywords"][4]["keyword"] = "Glad"
    data[1]["keywords"][5]["keywordScore"] = "10"
    data[1]["keywords"][5]["keyword"] = "Greeting"

    data[2]["topicName"]= "Introduction"
    data[2]["topicDuration"]= "42"
    data[2]["startTime"] = "00:00:39"
    data[2]["events"] = [{},{}]
    data[2]["events"][0]["eventTime"] = "00:00:53"
    data[2]["events"][0]["eventName"] = "Introducing sex hormones"
    data[2]["events"][1]["eventTime"] = "00:00:57"
    data[2]["events"][1]["eventName"] = "Introducing testosterone"

    data[2]["sentences"]=[{
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
        }]


    data[2]["keywords"] = [{},{},{},{},{},{},{}]
    data[2]["keywords"][0]["keywordScore"] = "6"
    data[2]["keywords"][0]["keyword"] = "hormones"
    data[2]["keywords"][1]["keywordScore"] = "8"
    data[2]["keywords"][1]["keyword"] = "sex"
    data[2]["keywords"][2]["keywordScore"] = "8"
    data[2]["keywords"][2]["keyword"] = "testosterone"
    data[2]["keywords"][3]["keywordScore"] = "5"
    data[2]["keywords"][3]["keyword"] = "price"
    data[2]["keywords"][4]["keywordScore"] = "4"
    data[2]["keywords"][4]["keyword"] = "natural"
    data[2]["keywords"][5]["keywordScore"] = "3"
    data[2]["keywords"][5]["keyword"] = "free"
    data[2]["keywords"][6]["keywordScore"] = "10"
    data[2]["keywords"][6]["keyword"] = "Introducing"

    data[3]["topicName"]= "Advertisement"
    data[3]["topicDuration"]= "137"
    data[3]["startTime"] = "00:01:32"
    data[3]["events"] = [{},{},{},{}]
    data[3]["events"][0]["eventTime"] = "00:01:36"
    data[3]["events"][0]["eventName"] = "sponsor website"
    data[3]["events"][1]["eventTime"] = "00:01:50"
    data[3]["events"][1]["eventName"] = "hemp protein"
    data[3]["events"][2]["eventTime"] = "00:02:42"
    data[3]["events"][2]["eventName"] = "lower toxicity"
    data[3]["events"][3]["eventTime"] = "00:03:04"
    data[3]["events"][3]["eventName"] = "vanilla acai"
    data[3]["sentences"] = [{
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
        }]
    data[3]["keywords"] = [{},{},{},{},{}]
    data[3]["keywords"][0]["keywordScore"] = "9"
    data[3]["keywords"][0]["keyword"] = "onnit"
    data[3]["keywords"][1]["keywordScore"] = "8"
    data[3]["keywords"][1]["keyword"] = "protein"
    data[3]["keywords"][2]["keywordScore"] = "6"
    data[3]["keywords"][2]["keyword"] = "medicine"
    data[3]["keywords"][3]["keywordScore"] = "5"
    data[3]["keywords"][3]["keyword"] = "flavor"
    data[3]["keywords"][4]["keywordScore"] = "10"
    data[3]["keywords"][4]["keyword"] = "Advertisement"

    data[4]["topicName"]= "Review"
    data[4]["topicDuration"]= "42"
    data[4]["startTime"] = "00:03:53"
    data[4]["events"] = [{},{}]
    data[4]["events"][0]["eventTime"] = "00:03:55"
    data[4]["events"][0]["eventName"] = "Five star rating"
    data[4]["events"][1]["eventTime"] = "00:04:31"
    data[4]["events"][1]["eventName"] = "Go to show"
    data[4]["sentences"] = [{
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
    data[4]["keywords"] = [{},{},{},{},{}]
    data[4]["keywords"][0]["keywordScore"] = "8"
    data[4]["keywords"][0]["keyword"] = "Itunes"
    data[4]["keywords"][1]["keywordScore"] = "9"
    data[4]["keywords"][1]["keyword"] = "Awesome"
    data[4]["keywords"][2]["keywordScore"] = "8"
    data[4]["keywords"][2]["keyword"] = "Podcast"
    data[4]["keywords"][3]["keywordScore"] = "5"
    data[4]["keywords"][3]["keyword"] = "Book"
    data[4]["keywords"][4]["keywordScore"] = "10"
    data[4]["keywords"][4]["keyword"] = "Review"

    #delete '\u0080\u009d, \u0080\u0099

    json.dump(data, output)