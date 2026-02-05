# Skill: generate media

## Purpose

Create engaging content (text, images, videos) for social media.

## Input

{
"content_type": "text | image | video",
"topic": "string",
"style": "string"
}

## Output

{
"status": "success | error",
"content_url": "string",
"confidence": 0.0
}

## Tools Used

- MCP Content Generation API

# Description

This skill generates media content based on the specified content type, topic, and style using the MCP Content Generation API. It returns the status of the content generation process, a URL to access the generated content, and a confidence score indicating the quality of the generated media. This skill is ideal for creating engaging and relevant content for social media platforms, marketing campaigns, or any other context where dynamic content is needed.
