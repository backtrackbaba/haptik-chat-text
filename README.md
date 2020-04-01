# Haptik Chat

## Problem Statement:

Get top 3 users from chat file

## Design Decisions

### Why download the file instead of directly loading in memory?

   As this is a small file with just a little over 2kb in size, loading it directly into memory won't matter much. Keeping in mind a scalable solution, I chose to download the file first and then load it in memory as described below

### Why chunking of files while downloading?

   The way requests works is, when you hit any url, the data is first loaded onto memory and then we could either process it directly or download/save it somewhere. By enabling the streaming of requests, it becomes possible to get only predefined chunks of data in memory which is regularly flushed out to disk while saving the file. Current size set is 8192 kb which means at any point while downloading only 8192 kb of data would be in memory of the file.
   
### Why reading lines from file pointer instead of `readlines()` method?

   The readlines method loads the whole file into memory and then reads line by line. In order for it to be efficient, we are opening the file contextually which manages the file closing operations well. And by reading from the filepointer, you essentially read only one line at a time which again saves a lot of memory.
    
    
### A better approach

A better approach would be using Redis' Sorted sets which essentially gives you a sorted dictionary by default with the ability to slice and dice to get the top `n` users

