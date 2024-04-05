from typing import Optional, overload, Literal
from openai.types.chat import ChatCompletionSystemMessageParam as SystemMessage, ChatCompletionAssistantMessageParam as AssistantMessage, ChatCompletionUserMessageParam as UserMessage
    
Messages = SystemMessage | AssistantMessage | UserMessage

InterviewLog = list[Messages]
InterviewLogToAppend = Optional[InterviewLog]

MessageMap = {
    "system": SystemMessage,
    "assistant": AssistantMessage,
    "user": UserMessage
}