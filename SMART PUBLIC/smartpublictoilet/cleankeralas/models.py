from django.db import models

class searchtoilets(models.Model):
    s_name=models.CharField(max_length=200)
    s_status=models.CharField(max_length=200)
    s_rate=models.CharField(max_length=200)
    s_image=models.ImageField(upload_to= 'search')
    s_serial=models.CharField(max_length=200)
    
    

    def __str__(self):
        return f"{self.s_name} ({self.s_serial})"  # Display s_name first, followed by s_serial in parentheses

    
class books(models.Model):
    c_name=models.CharField(max_length=200)
    s_phone=models.CharField(max_length=10)
    s_name=models.ForeignKey(searchtoilets, on_delete=models.CASCADE)
    s_email=models.EmailField()
    
    toilet_by_serial=models.ForeignKey(searchtoilets, on_delete=models.CASCADE ,related_name='books_by_serial' ,null=True, blank=True)

    
    def __str__(self):
        return f"{self.s_name} ({self.s_serial})"  # Display s_name first, followed by s_serial in parentheses

class reports(models.Model):
    r_name=models.CharField(max_length=200)
    r_phone=models.CharField(max_length=10)
    s_name=models.ForeignKey(searchtoilets, on_delete=models.CASCADE)
    r_email=models.EmailField()
    t_report=models.CharField(max_length=255, null=True)
    t_by_serial=models.ForeignKey(searchtoilets, on_delete=models.CASCADE ,related_name='reports_by_serial' ,null=True, blank=True)


