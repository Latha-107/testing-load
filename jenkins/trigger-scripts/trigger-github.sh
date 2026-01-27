curl -X POST \
-H "Authorization: token $GITHUB_TOKEN" \
https://api.github.com/repos/ORG/REPO/actions/workflows/main.yml/dispatches \
-d '{"ref":"main"}'
