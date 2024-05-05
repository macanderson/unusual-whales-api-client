openapi-python-client generate \
  --path openapi.yaml \
  --custom-template-path=templates \
  --config=config.yml \
  --meta=poetry

openapi-python-client update \
  --path openapi.yaml \
  --custom-template-path=templates \
  --config=config.yml