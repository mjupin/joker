from django.db import models

class Reviewer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Suite(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Browser(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.name

class TestResult(models.Model):
    run_date = models.DateTimeField('run time and date', unique=True)
    overall_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    def __str__(self):
        return self.run_date.strftime("%m-%d-%Y %H:%M:%S")

class BrowserReport(models.Model):
    browser = models.ForeignKey(Browser, on_delete=models.CASCADE)
    pass_count = models.IntegerField()
    fail_count = models.IntegerField()
    skip_count = models.IntegerField()
    defects = models.CharField(max_length=100, blank=True)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rca = models.CharField(max_length=2000, blank=True)
    action_plan = models.CharField(max_length=1000, blank=True)
    hostname = models.CharField(max_length=50)
    report_path = models.URLField(blank=True)
    test = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    def __str__(self):
        return self.browser.name