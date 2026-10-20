// Implement a timer class given a timer interface

interface TimerType {
    // starts the timer, includes restart
    startTimer:  () => void, 
    // stops the timer 
    pauseTimer: () => void,
    // resets it back to initial state
    resetTimer: () => void, 
    // returns the current time
    getCurrentTime: () => number, 
    // prints the current time in "hh:mm:ss" format
    printCurrentTime: () => void, 
}


/**
 * If the problem doesn't provide examples, then create your own! You need this to understand any problem 
 * Example
 * 1. S, 1 sec pass, P, getCurrentTime => 1
 * 2. 1 sec pass, getCurrentTime => 1 
 * 3. S, 1 sec pass, P, getCurrentTime => 2
 * 
 * How do we represent the increase of time? Current - previous  -> Date.now()
 * 1. P current time - S currentTime
 * 2. use a isPaused flag and set currentTime to Date.now() - prevStart
 * 3. same as 1 
 */

class Timer { 
    currentTime = 0; 
    prevStart = 0; 
    isPaused = false; 

    // set prevStart Time
    startTimer() {
        this.isPaused = false; 
        this.prevStart = Date.now()
    }
    // add to currentTime, set flag
    pauseTimer() {
        this.currentTime += Date.now() - this.prevStart;
        this.isPaused = true; 
    }
    // reset all instance 
    resetTimer() {
        this.currentTime = 0; 
        this.prevStart = 0; 
        this.isPaused = false; 
    }
    // need to return Date.now() - prevStart;
    // if paused then need to return 
    getCurrentTime() {
        if (this.isPaused) return this.currentTime;
        return Date.now() - this.prevStart + this.currentTime; 
    } 
}

const wait = (ms: number) =>
    new Promise<void>((resolve) => setTimeout(resolve, ms));

async function demo() {
    const timer = new Timer();

    // 1
    timer.startTimer();
    await wait(1000);
    timer.pauseTimer();
    console.log(timer.getCurrentTime()); // 1

    // 2
    await wait(1000);
    console.log(timer.getCurrentTime()); // 1

    // 3
    timer.startTimer();
    await wait(1000);
    console.log(timer.getCurrentTime()); // 2
}

demo();

export {};

