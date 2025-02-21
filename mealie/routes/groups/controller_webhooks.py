from functools import cached_property

from fastapi import APIRouter, Depends
from pydantic import UUID4

from mealie.routes._base.base_controllers import BaseUserController
from mealie.routes._base.controller import controller
from mealie.routes._base.mixins import HttpRepo
from mealie.schema import mapper
from mealie.schema.group.webhook import CreateWebhook, ReadWebhook, SaveWebhook
from mealie.schema.query import GetAll

router = APIRouter(prefix="/groups/webhooks", tags=["Groups: Webhooks"])


@controller(router)
class ReadWebhookController(BaseUserController):
    @cached_property
    def repo(self):
        return self.repos.webhooks.by_group(self.group_id)

    @property
    def mixins(self) -> HttpRepo:
        return HttpRepo[CreateWebhook, SaveWebhook, CreateWebhook](self.repo, self.deps.logger)

    @router.get("", response_model=list[ReadWebhook])
    def get_all(self, q: GetAll = Depends(GetAll)):
        return self.repo.get_all(start=q.start, limit=q.limit, override=ReadWebhook)

    @router.post("", response_model=ReadWebhook, status_code=201)
    def create_one(self, data: CreateWebhook):
        save = mapper.cast(data, SaveWebhook, group_id=self.group.id)
        return self.mixins.create_one(save)

    @router.get("/{item_id}", response_model=ReadWebhook)
    def get_one(self, item_id: UUID4):
        return self.mixins.get_one(item_id)

    @router.put("/{item_id}", response_model=ReadWebhook)
    def update_one(self, item_id: UUID4, data: CreateWebhook):
        return self.mixins.update_one(data, item_id)

    @router.delete("/{item_id}", response_model=ReadWebhook)
    def delete_one(self, item_id: UUID4):
        return self.mixins.delete_one(item_id)  # type: ignore
