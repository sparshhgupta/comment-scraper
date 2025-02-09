from cluster_sentiment import analyze_all_themes
import json


# Load the keyword sets from the JSON file
def load_keywords(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Use the loaded keywords in your function
def generate_actionable_insights(keywords_themes):
    keyword_data = load_keywords("related_keywords.json")
    
    audio_related_keywords = set(keyword_data["audio_related_keywords"])
    video_related_keywords = set(keyword_data["video_related_keywords"])
    content_related_keywords = set(keyword_data["content_related_keywords"])
    technical_related_keywords = set(keyword_data["technical_related_keywords"])
    positive_feedback_keywords = set(keyword_data["positive_feedback_keywords"])

    actionable_insights = []
    theme_sentiments = analyze_all_themes(keywords_themes)  # Get sentiment for each theme

    for theme, keywords in keywords_themes.items():
        sentiment = theme_sentiments.get(theme)  # Get the sentiment for the theme

        # Check the keywords in the theme and categorize them
        audio_issues = [keyword for keyword in keywords if keyword in keyword_data.get("audio_related_keywords", [])]
        video_issues = [keyword for keyword in keywords if keyword in keyword_data.get("video_related_keywords", [])]
        content_issues = [keyword for keyword in keywords if keyword in keyword_data.get("content_related_keywords", [])]
        technical_issues = [keyword for keyword in keywords if keyword in keyword_data.get("technical_related_keywords", [])]
        positive_feedback = [keyword for keyword in keywords if keyword in keyword_data.get("positive_feedback_keywords", [])]
        emotional_background_issues = [keyword for keyword in keywords if keyword in keyword_data.get("emotional_background_keywords", [])]
        general_feedback = [keyword for keyword in keywords if keyword in keyword_data.get("general_feedback_keywords", [])]
        interaction_related_issues = [keyword for keyword in keywords if keyword in keyword_data.get("interaction_related_keywords", [])]
        platform_related_issues = [keyword for keyword in keywords if keyword in keyword_data.get("platform_related_keywords", [])]

        if sentiment == 'negative':
            if audio_issues:
                actionable_insights.append(
                    f"Insight '{theme}': A significant number of comments mention audio issues (e.g., {', '.join(audio_issues)}). "
                    "Consider improving the mic quality, adjusting volume levels, or adding noise cancellation features to enhance audio clarity."
                )

            if video_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Comments indicate video quality concerns (e.g., {', '.join(video_issues)}). "
                    "Consider improving video lighting, camera resolution, or focus settings to enhance the visual experience."
                )

            if content_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Viewer comments suggest content-related issues (e.g., {', '.join(content_issues)}). "
                    "You may want to consider speeding up the pace, adding more dynamic scenes, or improving content flow to maintain engagement."
                )

            if technical_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Technical issues such as feedback or interference were mentioned (e.g., {', '.join(technical_issues)}). "
                    "Consider upgrading equipment, reducing interference, and ensuring smooth technical operations during production."
                )

            if positive_feedback:
                actionable_insights.append(
                    f"Insight '{theme}': Positive feedback highlights strengths in your content (e.g., {', '.join(positive_feedback)}). "
                    "Continue focusing on these aspects to deliver high-quality and engaging content that resonates with your audience."
                )

            if emotional_background_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Comments indicate emotional responses such as frustration or inspiration (e.g., {', '.join(emotional_background_issues)}). "
                    "Consider how your content can address negative sentiments or amplify positive emotional engagement."
                )

            if general_feedback:
                actionable_insights.append(
                    f"Insight '{theme}': General feedback provides insights into viewer perceptions (e.g., {', '.join(general_feedback)}). "
                    "Use this feedback to refine your overall content and improve user satisfaction."
                )

            if interaction_related_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Interaction-related comments suggest areas to improve engagement (e.g., {', '.join(interaction_related_issues)}). "
                    "Consider encouraging more comments, questions, or interactions to foster a stronger community."
                )

            if platform_related_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Platform-related concerns were mentioned (e.g., {', '.join(platform_related_issues)}). "
                    "Consider optimizing content for the platform's algorithm, improving compatibility, or addressing specific platform-related feedback."
                )

        # For positive sentiment, emphasize the strengths
        elif sentiment == 'positive':
            if audio_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive feedback highlights audio strengths (e.g., {', '.join(audio_issues)}). "
                    "Your audience appreciates the clarity, balance, and overall quality of your audio. Keep up the great work in this area!"
                )

            if video_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive comments indicate satisfaction with the video quality (e.g., {', '.join(video_issues)}). "
                    "Your viewers find the visuals appealing. Continue enhancing your camera work, lighting, and video resolution to maintain a high standard."
                )

            if content_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive content-related feedback emphasizes the engaging nature of your content (e.g., {', '.join(content_issues)}). "
                    "Your audience finds your content interesting and enjoyable. Keep delivering value by maintaining the balance between information and entertainment."
                )

            if technical_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive feedback suggests that your technical setup is appreciated (e.g., {', '.join(technical_issues)}). "
                    "Your audience is impressed with the smooth technical execution. Keep up the good work with your setup and ensure the consistency of this high quality."
                )

            if interaction_related_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive interaction-related feedback highlights how well you engage with your audience (e.g., {', '.join(interaction_related_issues)}). "
                    "Your viewers appreciate your responsiveness and the interactive nature of your content. Keep fostering this connection to build a loyal audience."
                )

            if platform_related_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive feedback about platform usage and content visibility (e.g., {', '.join(platform_related_issues)}). "
                    "Your content is performing well on the platform, and viewers are enjoying the experience. Continue optimizing for platform algorithms and user engagement."
                )

            if emotional_background_issues:
                actionable_insights.append(
                    f"Insight '{theme}': Positive emotional responses from viewers (e.g., {', '.join(emotional_background_issues)}). "
                    "Your content resonates emotionally with your audience. Keep producing content that evokes such positive emotions to strengthen viewer loyalty."
                )

            if general_feedback:
                actionable_insights.append(
                    f"Insight '{theme}': Positive general feedback reflects high viewer satisfaction (e.g., {', '.join(general_feedback)}). "
                    "Your audience is pleased with your work and enjoys your content. Continue delivering high-quality content and engaging your community."
                )

    return actionable_insights


# def generate_actionable_insights(keywords_themes):
#     actionable_insights = []
#     theme_sentiments = analyze_all_themes(keywords_themes)

#     for theme, keywords in keywords_themes.items():
#         # Collect the keyword types for insight generation
#         audio_related_keywords = {"mic", "audio", "sound", "volume", "low", "bad", "echo", "background noise"}
#         video_related_keywords = {"camera", "quality", "focus", "clear", "sharp", "video", "lighting"}
#         content_related_keywords = {"boring", "slow", "uninteresting", "pacing", "engaging", "dynamic"}
#         technical_related_keywords = {"noise", "echo", "feedback", "disturbance", "poor"}
#         positive_feedback_keywords = {"insightful", "interesting", "learned", "educational", "engaging"}

#         # Check the keywords in the theme and categorize them
#         audio_issues = any(keyword in audio_related_keywords for keyword in keywords)
#         video_issues = any(keyword in video_related_keywords for keyword in keywords)
#         content_issues = any(keyword in content_related_keywords for keyword in keywords)
#         technical_issues = any(keyword in technical_related_keywords for keyword in keywords)
#         positive_feedback = any(keyword in positive_feedback_keywords for keyword in keywords)

#         # Generate insights based on found keywords
#         if audio_issues:
#             actionable_insights.append(
#                 f"Theme '{theme}': A significant number of comments mention audio issues (e.g., 'mic', 'sound'). Consider improving the mic quality, adjusting volume levels, or adding noise cancellation features to enhance audio clarity."
#             )

#         if video_issues:
#             actionable_insights.append(
#                 f"Theme '{theme}': Comments indicate video quality concerns (e.g., 'focus', 'camera'). Consider improving video lighting, camera resolution, or focus settings to enhance the visual experience."
#             )

#         if content_issues:
#             actionable_insights.append(
#                 f"Theme '{theme}': Viewer comments suggest pacing issues (e.g., 'boring', 'slow'). You may want to consider speeding up the pace, adding more dynamic scenes, or improving content flow to maintain engagement."
#             )

#         if technical_issues:
#             actionable_insights.append(
#                 f"Theme '{theme}': Technical issues such as background noise or poor audio quality were mentioned. Consider upgrading your microphone, reducing background noise, and ensuring clean audio capture during recording."
#             )

#         if positive_feedback:
#             actionable_insights.append(
#                 f"Theme '{theme}': Positive feedback suggests your content is insightful and engaging. Continue focusing on delivering high-quality educational content that resonates with your audience."
#             )

#     return actionable_insights
