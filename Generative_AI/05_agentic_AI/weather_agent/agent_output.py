from pydantic import BaseModel, Field
from typing import Optional


class myOutputFormat(BaseModel):

    step : str = Field(..., description="The ID of the step can be PLAN, START, OUPUT, TOOL")
    content : Optional[str] = Field(None, description="The optional string content for the step")
    tool : Optional[str] = Field(None, description="The ID of the tool to call")
    input : Optional[str] = Field(None, description='The input param for the tool')