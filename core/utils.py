import uuid

def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")
    return code

# duration = datetime.now(timezone.utc).astimezone() - self.date
        # duration = date.today() - self.date

        # print('Adjusted date', datetime.today())
        # print('Real example date', datetime.now(timezone.utc).astimezone())
        # print('This is the self.date', self.date)
        # # duration = datetime.now(pytz.UTC) - self.date
 
        # # duration_in_s = duration.total_seconds()
        # # hours = divmod(duration_in_s, 3600)[0]
        # # print('hours', hours)
        # # if hours < 24 and hours >= 0:
        # duration = duration.seconds//3600
        # if duration == 0:

        #     self.question += 1

        #     if self.question == 2 and self.active == False:
        #         self.length += 1
        #         self.active = True
        #         self.profile.coins += 10
        #         self.profile.save()
        #         print('It is working with the coins')
        #     super().save(*args, **kwargs)

        # elif duration > 0:
        #     self.question = 0
        #     self.active = False