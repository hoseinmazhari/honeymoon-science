class user_pas_cols():
    site = "site"
    domain = 'domain'
    username = 'username'
    have_username = 'have username'
    password = 'password'
    have_password = 'have password'
def get_index_user_pass(df):
    this_class = user_pas_cols()
    this_itter = -1
    for col in df.columns:
        this_itter += 1
        if col == this_class.site:
            this_class.site = this_itter
        elif col == this_class.domain:
            this_class.domain = this_itter
        elif col == this_class.username:
            this_class.username = this_itter
        elif col == this_class.have_username:
            this_class.have_username = this_itter
        elif col == this_class.password:
            this_class.password = this_itter
        elif col == this_class.have_password:
            this_class.have_password = this_itter
    return this_class

