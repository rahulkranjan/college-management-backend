from django.db import models


class Branches(models.Model):
    branch_name = models.CharField(
        max_length=100, default='', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'branches'

    def __str__(self):
        return str(self.branch_name)


class College(models.Model):
    college_name = models.CharField(
        max_length=100, default='', blank=True, null=True)
    college_short_name = models.CharField(
        max_length=10, default='', blank=True, null=True)
    state = models.CharField(max_length=100, default='', blank=True, null=True)
    avilable_branch = models.ForeignKey(Branches, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    modified_at = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'college'

    def __str__(self):
        return str(self.college_name)
