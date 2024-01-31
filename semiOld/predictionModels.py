from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.svm import SVC


def RFModel(train_x, train_y, test_x, test_y, verify_x, verify_y):
    rf = RandomForestClassifier(
        n_estimators=100,
        criterion='entropy',
        min_samples_split=2,
        min_samples_leaf=1,
        bootstrap=True
    )

    rf.fit(train_x, train_y['Label'])
    rf_pred = rf.predict(test_x)

    accuracy_test = accuracy_score(test_y, rf_pred)
    precision_test = precision_score(test_y, rf_pred, zero_division=1)
    recall_test = recall_score(test_y, rf_pred, zero_division=1)
    f1_test = f1_score(test_y, rf_pred, zero_division=1)
    conf_test = confusion_matrix(test_y, rf_pred)

    rf_pred_new = rf.predict(verify_x)

    accuracy_verify = accuracy_score(verify_y, rf_pred_new)
    precision_verify = precision_score(verify_y, rf_pred_new, zero_division=1)
    recall_verify = recall_score(verify_y, rf_pred_new, zero_division=1)
    f1_verify = f1_score(verify_y, rf_pred_new, zero_division=1)
    conf_verify = confusion_matrix(verify_y, rf_pred_new)

    return  accuracy_test, precision_test, recall_test, f1_test, accuracy_verify, precision_verify, recall_verify, f1_verify, conf_test, conf_verify


def SVCModel(train_x, train_y, test_x, test_y, verify_X, verify_y):
    svc = SVC(
        C=1,
        kernel='rbf',
        gamma=0.001,
        max_iter=-1
    )

    svc.fit(train_x, train_y['Label'])
    svc_pred = svc.predict(test_x)

    accuracy_test = accuracy_score(test_y, svc_pred)
    precision_test = precision_score(test_y, svc_pred, zero_division=1)
    recall_test = recall_score(test_y, svc_pred, zero_division=1)
    f1_test = f1_score(test_y, svc_pred, zero_division=1)
    conf_test = confusion_matrix(test_y, svc_pred)

    svc_pred_new = svc.predict(verify_X)

    accuracy_verify = accuracy_score(verify_y, svc_pred_new)
    precision_verify = precision_score(verify_y, svc_pred_new, zero_division=1)
    recall_verify = recall_score(verify_y, svc_pred_new, zero_division=1)
    f1_verify = f1_score(verify_y, svc_pred_new, zero_division=1)
    conf_verify = confusion_matrix(verify_y, svc_pred_new)

    return accuracy_test, precision_test, recall_test, f1_test, accuracy_verify, precision_verify, recall_verify, f1_verify, conf_test, conf_verify


def AdaRFModel(train_x, train_y, test_x, test_y, verify_x, verify_y):
    ada1 = AdaBoostClassifier(
        estimator=RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            criterion='entropy',
            min_samples_split=2,
            min_samples_leaf=2,
            max_features='sqrt',
            bootstrap=True,
        ),
        n_estimators=100,
        learning_rate=0.1
    )
    ada1.fit(train_x, train_y['Label'])

    ada_pred1 = ada1.predict(test_x)

    accuracy_test = accuracy_score(test_y, ada_pred1)
    precision_test = precision_score(test_y, ada_pred1)
    recall_test = recall_score(test_y, ada_pred1)
    f1_test = f1_score(test_y, ada_pred1)
    conf_test = confusion_matrix(test_y, ada_pred1)

    ada_pred_new = ada1.predict(verify_x)

    accuracy_verify = accuracy_score(verify_y, ada_pred_new)
    precision_verify = precision_score(verify_y, ada_pred_new)
    recall_verify = recall_score(verify_y, ada_pred_new)
    f1_verify = f1_score(verify_y, ada_pred_new)
    conf_verify = confusion_matrix(verify_y, ada_pred_new)

    return accuracy_test, precision_test, recall_test, f1_test, accuracy_verify, precision_verify, recall_verify, f1_verify, conf_test, conf_verify