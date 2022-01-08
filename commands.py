"""
    # Run image as container and call test runner + linter
    docker-compose run app sh -c "python manage.py test && flake8"  
"""