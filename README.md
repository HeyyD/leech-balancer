# Leech Balancer

The **Leech Balancer** plugin for Anki is designed to prevent cards that you are capable of learning from turning into leeches. Even when you consistently answer cards correctly, their lapse count remains unchanged. Sometimes, cards become leeches because of a bad day, a brain fart, or simply because it's been a while since you reviewed them. Especially when you first start to learn a card, there might be many days where you fail it before it starts to click. This doesn't necessarily mean that the card is poor or that the user is unable to learn it.

This plugin reduces the lapse count of a card after you demonstrate consistent success with it. By ensuring that lapses are reduced for cards you consistently answer correctly, this plugin helps you focus on learning rather than penalizing temporary setbacks.

### Why Use This Plugin?

This plugin is ideal for learners who:
- Want to rehabilitate potential leech cards that they can learn with consistent effort.
- Understand that occasional mistakes shouldn't permanently mark a card as problematic.

## Settings

You can customize the plugin's behavior through its configuration:

### Required Correct Answers
- **Purpose**: Sets the number of consecutive correct answers needed to reduce a card's lapse count.
- **Default Value**: `3`

### Show Notifications
- **Purpose**: Enables or disables toast notifications when a lapse is reduced.
- **Default Value**: `true`

### How to Configure
1. Open Anki.
2. Go to `Tools > Leech Balancer Config`.
3. Adjust the settings and save.

