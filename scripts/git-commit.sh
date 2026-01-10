#!/bin/bash
set -e

# shellcheck disable=SC1091
. ./release.env

if [ -z "$ISSUE_TO_CLOSE" ]; then
  GIT_MESSAGE="$COMMIT_MESSAGE"
else
  GIT_MESSAGE="$COMMIT_MESSAGE, Close $ISSUE_TO_CLOSE"
fi

set -x
git commit -m "$GIT_MESSAGE"

