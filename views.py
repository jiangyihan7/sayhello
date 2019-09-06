#视图函数
from flask import flash,url_for,render_template,redirect
from sayhello import db,app
from sayhello.models import Message
from sayhello.forms import HelloForm

@app.route('/',methods=['GET','POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body,name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)

