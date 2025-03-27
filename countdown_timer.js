function countdown(seconds) {
    let interval = setInterval(() => {
        console.log(`⏳ Time left: ${seconds} seconds`);
        seconds--;

        if (seconds < 0) {
            clearInterval(interval);
            console.log("🎉 Time's up!");
        }
    }, 1000);
}

countdown(10); // Change 10 to any number of seconds
