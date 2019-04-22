
// Store the 3 buttons in some object
var buttons = {
    play: document.getElementById("btn-play"),
    pause: document.getElementById("btn-pause"),
};

// Create an instance of wave surfer with its configuration
var Spectrum = WaveSurfer.create({
    container: '#audio-spectrum',
    progressColor: "#686868",
    barWidth: 1,
    barHeight: 0.5,
    cursorColor: '#939292',
    cursorWidth: 2,
    
    
    pixelRatio: 1,

});

// Handle Play button
buttons.play.addEventListener("click", function() {
    Spectrum.play();
    buttons.play.disabled = true;
    buttons.pause.disabled = false;
    }, false);

// Handle Pause button
buttons.pause.addEventListener("click", function() {
    Spectrum.pause();
    buttons.pause.disabled = true;
    buttons.play.disabled = false;
}, false);





// Add a listener to enable the play button once it's ready
Spectrum.on('ready', function() {
    // Get the current progress according to the cursor position
    var currentProgress = Spectrum.getCurrentTime() / Spectrum.getDuration();

    // Reset graph
    Spectrum.empty();
    Spectrum.drawBuffer();
    // Set original position
    Spectrum.play();
    // Enable/Disable respectively buttons
    buttons.pause.disabled = false;
    buttons.play.disabled = true;
    
    
});

// If you want a responsive mode (so when the user resizes the window)
// the spectrum will be still playable
window.addEventListener("resize", function() {
    // Get the current progress according to the cursor position
    var currentProgress = Spectrum.getCurrentTime() / Spectrum.getDuration();

    // Reset graph
    Spectrum.empty();
    Spectrum.drawBuffer();
    // Set original position
    Spectrum.seekTo(currentProgress);

    // Enable/Disable respectively buttons
    buttons.pause.disabled = true;
    buttons.play.disabled = false;
   
}, false);


$(".play-img").click(function() {
    $(".audio-player").slideDown()
    audiouri = $( this ).parent().parent().find(".file-ref").attr("href");
    Spectrum.load(audiouri);
    
});
