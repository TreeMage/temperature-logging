from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class StorageConfig:
    path: str
    table: str


@dataclass_json
@dataclass(frozen=True)
class AppConfig:
    storage_config: StorageConfig