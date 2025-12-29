# Backend Engineering Intern – Case Study

**Name:** Rakesh Hokrani  
**Role:** Backend Engineering Intern  
**Date:** 29 Dec 2025  

## Overview
This repository contains my solution to the Backend Engineering Intern case study.
The goal was to analyze an existing API, design a scalable database schema, and
implement a low-stock alert system while handling incomplete requirements.

## Repository Structure
- `part1/` – Code review and fixed product creation API
- `part2/` – Database schema design and decisions
- `part3/` – Low-stock alerts API implementation
- `assumptions.md` – Assumptions and open questions

## Part 1: Code Review & Debugging
I identified multiple issues such as missing input validation, lack of SKU uniqueness
checks, unsafe decimal handling, and missing transaction management. The API was
refactored to ensure atomic database operations and production safety.

## Get requirements installed:
```bash
pip install -r requirements.txt
```
## How to Run Part 1
```bash
pip install flask flask-sqlalchemy
python product_api_fix.py
```
