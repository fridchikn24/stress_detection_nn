# stress_detection_nn
## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Contributing](#contributing)

## Project Overview

This project aims to:

- Build predictive models to estimate diamond prices based on their attributes.
- Provide visualizations to aid in understanding the relationships between different features and stress levels.

## Dataset

The dataset used in this project contains information about participants and their physical and psychological profiles , including:

participant_id:

    Unique identifier for each participant.
    Data type: Integer
    Range: 1 to 100 (as there are 100 participants)

day:

    The day of observation for each participant.
    Data type: Integer
    Range: 1 to 30 (each participant is observed over 30 days)

PSS_score:

    Perceived Stress Scale score, measuring stress levels.
    Data type: Integer
    Range: 10 to 40

Openness:

    Measure of openness to experience, a personality trait.
    Data type: Float
    Range: 1.0 to 5.0

Conscientiousness:

    Measure of conscientiousness, a personality trait.
    Data type: Float
    Range: 1.0 to 5.0

Extraversion:

    Measure of extraversion, a personality trait.
    Data type: Float
    Range: 1.0 to 5.0

Agreeableness:

    Measure of agreeableness, a personality trait.
    Data type: Float
    Range: 1.0 to 5.0

Neuroticism:

    Measure of neuroticism, a personality trait.
    Data type: Float
    Range: 1.0 to 5.0

sleep_time:

    The time (in hours) the participant went to sleep.
    Data type: Float
    Range: 5.0 to 9.0 hours

wake_time:

    The time (in hours) the participant woke up.
    Data type: Float
    Range: 5.0 to 9.0 hours

sleep_duration:

    The duration (in hours) the participant slept.
    Data type: Float
    Range: 6.0 to 9.0 hours

PSQI_score:

    Pittsburgh Sleep Quality Index (PSQI) score, measuring sleep quality.
    Data type: Integer
    Range: 1 to 5

call_duration:

    Total duration of phone calls for the day (in minutes).
    Data type: Float
    Range: 0 to 60 minutes

num_calls:

    Number of phone calls made during the day.
    Data type: Integer
    Range: 0 to 20 calls

num_sms:

    Number of SMS messages sent during the day.
    Data type: Integer
    Range: 0 to 50 messages

screen_on_time:

    Total screen-on time for the day (in hours).
    Data type: Float
    Range: 1.0 to 12.0 hours

skin_conductance:

    Measure of skin conductance, indicating arousal or stress response.
    Data type: Float
    Range: 0.5 to 5.0 µS (microsiemens)

accelerometer:

    Accelerometer data representing physical movement.
    Data type: Float
    Range: 0.1 to 2.5 g (g-force)

mobility_radius:

    The radius of mobility for the participant (in kilometers).
    Data type: Float
    Range: 0.1 to 1.5 km

mobility_distance:

    Total distance moved during the day (in kilometers).
    Data type: Float
    Range: 0.5 to 5.0 km

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request. Ensure that your contributions align with the project's coding standards and include appropriate tests.

