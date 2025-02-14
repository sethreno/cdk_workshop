import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import Stage

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack
from cdk_workshop.pipeline_stage import WorkshopPipelineStage


class WorkshopPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        pipeline = CodePipeline(
            self,
            "CdkWorkshopPipeline",
            pipeline_name="CdkWorkshopPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.connection(
                    "sethreno/cdk_workshop",
                    "main",
                    connection_arn="arn:aws:codeconnections:us-east-2:463470972895:connection/f6b0e51f-786e-4186-ae47-05e6d971126e",
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )

        deploy = WorkshopPipelineStage(self, "Deploy")
        pipeline.add_stage(deploy)
