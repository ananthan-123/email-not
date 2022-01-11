from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import activateModel, dataModel
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail
from smtplib import SMTPRecipientsRefused

html_remaindr = """

<html>
  <head>
    <style>
      body {
        padding: 20px;
        display: flex;
        color: #444444;
      }
      h1 {
        font-size: 40px;
        text-align: center;
      }
      .main {
        max-width: 323px;
        width: 100%;
        margin: auto;
      }
      p {
        font-size: 24px;
        justify-content: center;
        text-align: center;
      }
      img {
        width: 100%;
        margin: 30px 0;
      }
      .button {
        border-radius: 50%;
        background-color: #f9e44f;
        /* padding: 50px; */
        height: 120px;
        width: 120px;
        text-align: center;
        justify-content: center;
        margin: auto;
        display: flex;
        align-items: center;
      }
      .a {
        color: #444444;
        text-decoration: none;
      }
      .bot {
        text-align: center;
        margin-top: 20px;
      }
    </style>
  </head>
  <body>
    <div class="main">
      <h1>Hi there!</h1>
      <p>
        I just wanted to drop you a quick note to remind you about the product
        you would like to purchase. You'll find at the bottom for accessing the
        product.
      </p>
      <img
        src=""
        alt=""
      />
      <a href=""  class='a'>
        <div class="button">
          BUY NOW
        </div>
      </a>
      <div class="bot">
        If you have any question, please let me know and I'll be happy to assist
        you at koomzstore@gmail.com
      </div>
    </div>
  </body>
</html>

"""


@csrf_exempt
def storeData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        date = request.POST.get("date")
        link = request.POST.get("link")
        img_link = request.POST.get("img_link")

        print(name, mail)

        dat = dataModel()
        dat.name = name
        dat.email = mail
        dat.date = date
        dat.link = link
        dat.image_link = img_link
        dat.save()

        con = activateModel()
        con.data = dat
        con.save()

        subject, from_email, to = "Confirm remainder", "wintergarten123@gmail.com", mail
        msg_plain = ""
        msg_html = render_to_string(
            "templates/email_confirm.html", {"image": img_link, "activate": con.id}
        )

        try:
            send_mail(
                subject,
                msg_plain,
                from_email,
                [to],
                html_message=msg_html,
            )
            return JsonResponse(
                {
                    "res": "Success. A confirmation mail has been send to email. Please click on the confirmation link to confirm the remainder."
                }
            )
        except BadHeaderError:
            return JsonResponse(
                {"error": "Something went wrong! Please try again later."}
            )
        except SMTPRecipientsRefused:
            return JsonResponse({"error": "Mail sending failed. Invalid mail id."})
    else:
        return JsonResponse({"error": "Method not allowed"})


@csrf_exempt
def activate(request, activate_id):
    dat = len(activateModel.objects.filter(id=activate_id))
    if dat:
        dat1 = activateModel.objects.filter(id=activate_id)
        dat11 = dat1[0].data
        dat2 = dataModel.objects.filter(id=dat11)
        dat2.update(activated=True)
        dat1.delete()
        from_email = "wintergarten123@gmail.com"
        send_mail(
            "Activate link clicked",
            "A user clicked activate link",
            from_email,
            [from_email],
        )
        return render(request, "activate.html")
    else:
        return render(request, "error.html")
