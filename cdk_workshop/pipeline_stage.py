from constructs import Construct
from aws_cdk import Stage
from .cdk_workshop_stack import CdkWorkshopStack

class WorkshopPipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        service = CdkWorkshopStack(self, "WebService")

        self.hit_counter_url = service.hit_counter_url
        self.table_viewer_url = service.table_viewer_url
