# Module 11 - Google ADK (Android)

## What this code does
A button on the screen. When the student clicks it, the text
below the button changes to show an answer.

## The lifecycle (step by step)
1. User clicks the button (UI event)
2. onClick() runs
3. In a real app, this would send the question to the server over the network
4. The server would send back an answer
5. resultText.setText() updates what's shown on screen

## What I learned
Android apps react to user actions (like clicks) using something
called a listener (setOnClickListener). The screen only updates
when we explicitly tell a text box to change.

## Reference
https://developer.android.com/docs