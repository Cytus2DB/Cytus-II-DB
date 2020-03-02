#!/bin/bash

echo "================================="
echo "   Cytus II DB Build Tool V2.0   "
echo "          A.R.C.  Tech.          "
echo "================================="

rm -rf ./res/*/
rm -rf ./res/cache*
rm -rf ./web/.env
rm -rf ./web/dist
rm -rf ./web/public/*/

echo "Cache Cleaned."