#! /bin/bash
sed "s/\s*#[^!].*$/BALETED/" | sed "/^BALETED$/d" #| sed "s/BALETED//"
