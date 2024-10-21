# TODO#1


# TODO#2
# Load the TTS model


# TODO#3
# Limit available speakers to 3 females and 3 males


# TODO#4
# Set available languages to English and Spanish only


# TODO#5
# Default speaker and language


# TODO#6


# TODO#7


# Main Speech Synthesis Function
def generate_speech_with_timestamps(text, speaker, language):
    global last_generated_audio, last_generated_text
    output_path = "output/generated_speech.wav"
    start_time = time.time()

    # TODO#8


    # TODO#9


    # TODO#10


    # TODO#11


# Waveform Function
def generate_waveform():
    global last_generated_audio, last_generated_text

    if not last_generated_audio or not os.path.exists(last_generated_audio):
        return None, "No valid audio file found to generate waveform."

    samplerate, data = wavfile.read(last_generated_audio)
    time_axis = np.linspace(0, len(data) / samplerate, num=len(data))

    # Modern waveform style with gradient color
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='#1E1E1E')  # Dark background

    # Plot waveform with gradient
    ax.plot(time_axis, data, color='cyan', alpha=0.8, linewidth=1.2)

    # Styling grid and axes for a modern look
    ax.set_facecolor('#2E2E2E')  # Darker plot background
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_xlabel("Time (seconds)", color='white')
    ax.set_ylabel("Amplitude", color='white')

    # Set the title with trimmed text
    trimmed_text = trim_text(last_generated_text)
    ax.set_title(f"Waveform for text input: '{trimmed_text}'", color='white', fontsize=14)

    waveform_image_path = "output/waveform.png"
    plt.savefig(waveform_image_path, transparent=True)
    plt.close()

    return waveform_image_path, "Waveform generated successfully!"

# Button Click Event Handler
def on_generate_click(text, speaker, language):
    if not text:
        return None, "Please enter some text to generate speech.", "", gr.update(interactive=False)

    audio_path, word_count, speaker_name, lang, speech_length, duration = generate_speech_with_timestamps(text, speaker, language)

    # Format the text box content
    data_info = f"Word Count: {word_count}\nVoice: {speaker_name}\nLocalization: {lang}\nLength of Speech: {speech_length} seconds\nGeneration Duration: {duration} seconds"

    return audio_path, data_info, "Speech generation successful!", gr.update(interactive=True)

# Gradio Interface Setup
def setup_interface():
    with gr.Blocks() as app:
        # TODO#12

        
        with gr.Row():
            with gr.Column():
                # TODO#13
                # Indent your code to match the indention of this comment!

                with gr.Row():
                    # Create the dropdown component for the voice selection
                    speaker_dropdown = gr.Dropdown(choices=available_speakers, value=selected_speaker, label="Select Voice")
                    # Create the radio button gropu for the localization selection
                    language_radio = gr.Radio(choices=available_languages, value=selected_language, label="Select Localization")

            with gr.Column():
                # TODO#14
                # Indent your code to match the indention of this comment!

        with gr.Row():
            with gr.Column():
                # TODO#15
                # Indent your code to match the indention of this comment!

            with gr.Column():
                # TODO#16
                # Indent your code to match the indention of this comment!

        # Map the function of the Generate Speech button
        generate_button.click(
            on_generate_click, 
            inputs=[text_input, speaker_dropdown, language_radio], 
            outputs=[audio_output, data_info_display, status_message, generate_waveform_button]
        )

        # Map the function of the Generate Waveform button
        generate_waveform_button.click(
            generate_waveform, 
            outputs=[waveform_output, status_message]
        )

    return app

# TODO#17