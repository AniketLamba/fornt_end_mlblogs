from flask import Flask, render_template, request

app=Flask(__name__)

app.debug=True

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/supervised')
def supervised():
    return render_template('supervised.html')

@app.route('/unsupervised')
def unsupervised():
    return render_template('unsupervised.html')

@app.route('/reinforcement')
def reinforcement():
    return render_template('reinforcement.html')

@app.route('/classification')
def classification():
    return render_template('classification.html')

@app.route('/regression')
def regression():
    return render_template('regression.html')


@app.route('/clustering')
def clustering():
    return render_template('clustering.html')

@app.route('/association')
def association():
    return render_template('association.html')

@app.route('/logistic_regression')
def logistic_regression():
    return render_template('logistic_regression.html')

@app.route('/support_vector_machines')
def support_vector_machines():
    return render_template('support_vector_machines.html')

@app.route('/k_nearest_neighbor')
def k_nearest_neighbor():
    return render_template('k_nearest_neighbor.html')

@app.route('/naive_bayes')
def naive_bayes():
    return render_template('naive_bayes.html')

@app.route('/decision_trees')
def decision_trees():
    return render_template('decision_trees.html')

@app.route('/random_forest')
def random_forest():
    return render_template('random_forest.html')

@app.route('/one_vs_all')
def one_vs_all():
    return render_template('one_vs_all.html')

@app.route('/multinomial_logistic_regression')
def multinomial_logistic_regression():
    return render_template('multinomial_logistic_regression.html')

@app.route('/binary_relevance')
def binary_relevance():
    return render_template('binary_relevance.html')

@app.route('/classifier_chains')
def classifier_chains():
    return render_template('classifier_chains.html')

@app.route('/label_powerset')
def label_powerset():
    return render_template('label_powerset.html')

@app.route('/random_forest_based_models')
def random_forest_based_models():
    return render_template('random_forest_based_models.html')

if __name__=='__main__':
    app.run()