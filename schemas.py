from pydantic import BaseModel, constr


class ExampleNamesVal(BaseModel):
    name: constr(min_length=1, max_length=256)

    class Config:
        extra = 'forbid'
