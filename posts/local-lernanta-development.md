title: "Local Lernanta Development"
description: "Here's how I got a copy of Lernanta installed on my OS X dev machine."
created: 2011-06-19 12:50:48
---

![P2PU](http://media.jamiecurle.com/uploads/2011/06/19/blogimage/P2PU___University.850x600.jpg)


Back in January I blogged about [getting involved in the development of the new P2PU platform - Lernanta](http://jamiecurle.com/posts/peer-to-peer-university-development/), but time was against me.  Technically speaking it still is but the desire to get involved has not gone away and now that I'm running a class there I'm spotting bits and bobs that I'd love to implement.

The folks at [P2PU](http://p2pu.org/) are keen to drink their own 'kool aid' and so they've set up a [Contributing to Lernanta](http://p2pu.org/en/groups/introduction-to-contributing-to-lernata/) course for those interested in forking and adding back into the code base.  The signup task is to introduce yourself and the second task is to get [Lernanta](https://github.com/p2pu/lernanta)  installed and up and running. It was requested that we log our experience doing this and this is the context for this post.

## I forked

At some point I'm hoping the work that I do will be pulled back into the master repo so [I decided to fork Lernanta](https://github.com/jamiecurle/lernanta)

## Installing

I already have virtualenv and virtualenvwrapper installed so I didn't need to do most of the steps outlined - instead I just created a virtualenv and installed the requirements.  The requirements come in three files and the instructions direct users to install all three. There's no harm in this but in [requirements/dev.txt](https://github.com/p2pu/lernanta/blob/master/requirements/dev.txt) the dependancy on [requirements/prod.txt](https://github.com/p2pu/lernanta/blob/master/requirements/prod.txt) is stated, so you don't really need to install the production requirements because the dev requirements will do that for you.

The instructions state that the virtual environment be set up without using the site-packages from the global python installation. I didn't follow this instruction because PIL and MySQLdb are an arse to install on Snow Leopard.  Because of this I install them in the global site-packages python installation and let all virtualenv's use them from there. I don't think I'll run into much trouble with this because the versions I'm using are stable and I've got no need to upgrade.  ( I know that one day this will bite me ) 

## Migrations

I'm using MySQL ( with myisam tables I think) and I had a fair bit of trouble installing the migrations when setting up the database. I had to edit a number of the migration files to catch exceptions because MySQL couldn't find a number of constraints or keys. Here's a few examples


0005_auto__del_link__del_unique_link_project_url__del_field_project_descrip.py

<code lang="python">
class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Link', fields ['project', 'url']
        #db.delete_unique('projects_link', ['project_id', 'url'])

        # Deleting model 'Link'
        db.delete_table('projects_link')
        ...

</code>

0012_auto__add_field_project_preparation_status__del_unique_project_name.py

<code lang="python">

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Project', fields ['name']
        #db.delete_unique('projects_project', ['name'])
        pass

</code>

I know this isn't ideal to be just commenting the things out, but it does allow the migrations to run and get me up and running.

## Rabbit MQ

I have noticed that celery is in the dependancies and this has a dependancy on RabbitMQ which I don't have installed, so I'll be interested to see what challenges that throws up.

## Looking Forward

Yesterday I finally got [Vagrant](http://vagrantup.com/docs/getting-started/index.html) up and running and I think it'd be a great idea to put a box together that we could use as a replication the development enviroment. This maybe something I'll whip up to help me get to grips with either chef or puppet.

###0015_auto__del_projectmedia__del_field_participation_sign_up__add_field_par.py
<code lang="python">

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ProjectMedia'
        db.delete_table('projects_projectmedia')

        # Deleting field 'Participation.sign_up'
        db.delete_column('projects_participation', 'sign_up_id')

        # Adding field 'Participation.organizing'
        db.add_column('projects_participation', 'organizing', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Project.created_by'
        #db.delete_column('projects_project', 'created_by_id')
        ...


</code>


